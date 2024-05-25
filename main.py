from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy_garden.mapview import MapView, MapMarker
from geopy.geocoders import Nominatim
import ssl
import certifi
from threading import Thread
from kivy.clock import Clock
import geopy.geocoders
from kivy.core.window import Window
import pyperclip
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
import json
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
import random
import requests
import overpass

class SavePopup(Popup):
    def __init__(self, address, **kwargs):
        super().__init__(**kwargs)
        self.title = "Save Location"
        self.title_align = 'center'  # Center the title

        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))

        # Close button (X)
        close_button = Button(text='X', size_hint=(None, None), size=(dp(40), dp(40)))
        close_button.bind(on_release=self.dismiss)
        header_layout.add_widget(Label(text=self.title, size_hint=(1, 1)))
        header_layout.add_widget(close_button)

        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))

        # Address display (not editable)
        self.address_label = Label(text=f"Address: {address}", size_hint_y=None, height=dp(40))
        layout.add_widget(self.address_label)

        # Icon selection
        icon_selection = Button(text="Select Icon", size_hint_y=None, height=dp(40))
        icon_selection.bind(on_release=self.open_icon_dropdown)
        layout.add_widget(icon_selection)
        self.icon_dropdown = DropDown()

        # Adding icons to dropdown
        icons = ["home.png", "work.png", "family.png"]  # Path to icon images
        for icon in icons:
            btn = Button(text='', size_hint_y=None, height=dp(40))
            btn.bind(on_release=lambda btn: self.select_icon(icon))
            icon_image = Image(source=icon, size=(dp(40), dp(40)))
            btn.add_widget(icon_image)
            self.icon_dropdown.add_widget(btn)

        # Description input
        self.description_input = TextInput(hint_text="Enter description", multiline=False, size_hint_y=None,
                                           height=dp(40))
        layout.add_widget(self.description_input)

        # Save button
        save_button = Button(text="Save", size_hint_y=None, height=dp(40))
        save_button.bind(on_press=lambda instance: self.save_location(address))
        layout.add_widget(save_button)

        content_layout = BoxLayout(orientation='vertical')
        content_layout.add_widget(header_layout)
        content_layout.add_widget(layout)

        self.content = content_layout

    def open_icon_dropdown(self, instance):
        self.icon_dropdown.open(instance)

    def select_icon(self, icon):
        print(f"Selected icon: {icon}")
        self.icon_dropdown.dismiss()

    def save_location(self, address):
        description = self.description_input.text
        # Save the location locally
        saved_locations = load_saved_locations()
        saved_locations.append({"address": address, "description": description})
        save_saved_locations(saved_locations)

        print(f"Location '{address}' saved with description: {description}")
        self.dismiss()


class MapWithMarker(BoxLayout):
    def __init__(self, **kwargs):
        super(MapWithMarker, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = dp(20)  # Add Padding
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.address_input = TextInput(hint_text='Enter Address', size_hint=(0.7, None), height=dp(50), multiline=False, background_normal='', background_active='')
        self.address_input.bind(text=self.on_text)  # Bind text change
        self.address_input.bind(focus=self.on_focus)  # Bind focus
        self.copy_button = Button(text='Copy', size_hint=(None, None), size=(dp(100), dp(50)), background_color=(0.5, 0.5, 0.5, 1), background_normal='', background_down='')
        self.copy_button.bind(on_press=self.copy_text)

        # Speichern-Button
        self.save_button = Button(text='Save', size_hint=(None, None), size=(dp(100), dp(50)), background_color=(0.3, 0.6, 0.9, 1), background_normal='', background_down='')
        self.save_button.bind(on_press=self.open_save_popup)

        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=dp(50))
        input_layout.add_widget(self.address_input)
        input_layout.add_widget(self.copy_button)
        input_layout.add_widget(self.save_button)  # Add save button

        # Back button with arrow image
        back_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(None, None), size=(dp(50), dp(50)))
        back_button = Button(background_normal='arrow.png', background_down='arrow.png', size_hint=(None, None), size=(dp(50), dp(50)), background_color=(0.3, 0.6, 0.9, 1))
        back_button.bind(on_press=self.go_to_start)
        back_layout.add_widget(back_button)
        self.add_widget(back_layout)

        self.submit_button = Button(text='Submit', size_hint=(1, None), height=dp(50), background_color=(0.1, 0.7, 0.3, 1), background_normal='', background_down='')
        self.submit_button.bind(on_press=self.show_map)

        self.mapview = MapView(zoom=15, lat=0, lon=0, size_hint=[1,0.8])
        self.marker_new_address = MapMarker(lat=0, lon=0, color=(1, 0, 0, 1))
        self.mapview.add_widget(self.marker_new_address)
        self.marker_old_address = MapMarker(lat=0, lon=0, color=(0.478,0.478,0.478, 1))
        self.mapview.add_widget(self.marker_old_address)
        self.mapview.opacity = 0

        self.add_widget(input_layout)
        self.add_widget(self.submit_button)
        self.add_widget(self.mapview)

        # BoxLayout for address suggestions
        self.suggestion_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.add_widget(self.suggestion_layout)

        # Thread for geocoding query
        self.geocode_thread = None
        # Delay timer for geocoding match
        self.geocode_delay_timer = None
        # Delay time in seconds
        self.geocode_delay = 0.5

        # List for already added suggestions
        self.added_suggestions = set()

        self.address_input_focused = False  # Tracks focus of address input


    def go_to_start(self, instance):
        self.parent.parent.current = 'start'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_text(self, instance, value):
        # If delay timer is already running, cancel it
        if self.geocode_delay_timer:
            self.geocode_delay_timer.cancel()

        # Start a new delay timer
        self.geocode_delay_timer = Clock.schedule_once(lambda dt: self.start_geocode(value), self.geocode_delay)
        # Clear existing suggestions when text is empty
        if not value:
            self.suggestion_layout.clear_widgets()
            self.added_suggestions.clear()

    def on_focus(self, instance, value):
        # When focus is on address input, set the corresponding status
        if instance == self.address_input:
            self.address_input_focused = value

            # Clear existing suggestions when user starts entering a new address
            if not value:
                self.suggestion_layout.clear_widgets()
                self.added_suggestions.clear()

    def start_geocode(self, value):
        if value:
            if self.geocode_thread and self.geocode_thread.is_alive():
                # If a thread is already running, stop it
                self.geocode_thread.join()

            # Start a new thread for geocoding
            self.geocode_thread = Thread(target=self.geocode_address, args=(value,))
            self.geocode_thread.start()

    def geocode_address(self, value):
        ctx = ssl._create_unverified_context(cafile=certifi.where())
        geopy.geocoders.options.default_ssl_context = ctx
        loc = Nominatim(scheme='http', user_agent="Test")
        suggestions = loc.geocode(value, addressdetails=True, limit=10, exactly_one=False)

        if suggestions:
            # Notify main thread about found suggestions
            Clock.schedule_once(lambda dt: self.show_suggestions(suggestions))

    def show_suggestions(self, suggestions):
        # Clear existing suggestions when address input is finished
        if not self.address_input_focused:
            self.suggestion_layout.clear_widgets()
            self.added_suggestions.clear()
            return

        # Clear existing suggestions
        self.suggestion_layout.clear_widgets()
        self.added_suggestions.clear()

        for suggestion in suggestions:
            address = self.format_address(suggestion.raw)
            if address not in self.added_suggestions:
                btn = Button(text=address, size_hint_y=None, height=dp(44), background_normal='', background_color=(0.3, 0.6, 0.9, 1), background_down='')
                btn.bind(on_release=lambda btn: self.select_suggestion(btn.text))
                self.suggestion_layout.add_widget(btn)
                self.added_suggestions.add(address)

    def format_address(self, raw):
        address_parts = []

        address = raw.get('address')
        if address:
            street = address.get('road', '')
            city = address.get('city', '')
            country = address.get('country', '')

            if street:
                address_parts.append(street)

            if city:
                address_parts.append(city)

            if country:
                address_parts.append(country)

        return ', '.join(address_parts)

    def select_suggestion(self, address):
        self.address_input.text = address
        self.suggestion_layout.clear_widgets()  # Remove all suggestions after selection
        self.added_suggestions.clear()  # Reset list of added suggestions

    def show_map(self, instance):
        # Get the address from the input field
        address = self.address_input.text

        ctx = ssl._create_unverified_context(cafile=certifi.where())
        geopy.geocoders.options.default_ssl_context = ctx
        loc = Nominatim(scheme='http', user_agent="Test")
        location = loc.geocode(address)

        if location:
            # Generate random number of parks
            num_parks = random.randint(1, 10)  # Change the range as needed

            api = overpass.API()
            print(location.latitude)
            print(location.longitude)
            query = f"""
            node(around:500,{location.latitude},{location.longitude})["amenity"="restaurant"];
            out body;
            """

            # Get parks near the submitted address within a 5-minute radius
            #response = requests.get(
            #    f"http://overpass-api.de/api/interpreter?data=[out:json];node(around:300,,{location.longitude},{location.latitude})[amenity=park];out;")

            result = api.get(query)

            print("Overpass API Response:", result)  # Log the response

            if len(result['features']) != 0:
                data = result['features']
                print(data)
                amenities = []

                for feature in data:
                    # Extrahiere die Teile der Adresse aus den Tags des Features
                    street = feature['properties'].get('addr:street', '')
                    housenumber = feature['properties'].get('addr:housenumber', '')
                    city = feature['properties'].get('addr:city', '')
                    postcode = feature['properties'].get('addr:postcode', '')

                    # Füge die Adresse zur Liste der Annehmlichkeiten hinzu
                    address = f"{street} {housenumber}, {postcode} {city}"

                    print(address)
                    if address.strip() and address.strip() != "," and address.strip() != ", ":
                        amenities.append(address)

                print(amenities)
                if amenities:
                    # Choose a random park from the list
                    if len(amenities) >= num_parks:
                        selected_parks = random.sample(amenities, num_parks)
                    else:
                        selected_parks = amenities

                    # Set the input text to the selected park
                    selected_park = random.choice(selected_parks)
                    self.address_input.text = selected_park

                    # Get coordinates of the selected park
                    selected_location = loc.geocode(selected_park)
                    if selected_location:
                        self.marker_new_address.lat = selected_location.latitude
                        self.marker_new_address.lon = selected_location.longitude
                        self.marker_old_address.lat = location.latitude
                        self.marker_old_address.lon = location.longitude

                        min_lat = min(self.marker_new_address.lat, self.marker_old_address.lat)
                        max_lat = max(self.marker_new_address.lat, self.marker_old_address.lat)
                        min_lon = min(self.marker_new_address.lon, self.marker_old_address.lon)
                        max_lon = max(self.marker_new_address.lon, self.marker_old_address.lon)

                        center_lat = (min_lat + max_lat) / 2
                        center_lon = (min_lon + max_lon) / 2

                        self.mapview.center_on(center_lat, center_lon)

            self.mapview.opacity = 1

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def copy_text(self, instance):
        pyperclip.copy(self.address_input.text)
        instance.background_color = (0.5, 0.9, 0.5, 1)  # Green background color for feedback
        Clock.schedule_once(lambda dt: setattr(instance, 'background_color', (0.5, 0.5, 0.5, 1)), 0.5)  # Reset background color after 0.5 seconds

    def open_save_popup(self, instance):
        address = self.address_input.text
        save_popup = SavePopup(address=address)
        save_popup.open()


class ShowSavedLocationsPopup(Popup):
    def __init__(self, saved_locations, **kwargs):
        super().__init__(**kwargs)
        self.title = "Saved Locations"
        self.title_align = 'center'  # Center the title

        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))

        # Close button (X)
        close_button = Button(text='X', size_hint=(None, None), size=(dp(40), dp(40)))
        close_button.bind(on_release=self.dismiss)
        header_layout.add_widget(Label(text=self.title, size_hint=(1, 1)))
        header_layout.add_widget(close_button)

        layout = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(10))

        for location in saved_locations:
            address_label = Label(
                text=f"Address: {location['address']}, Description: {location.get('description', '')}")
            button_layout = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(10))
            copy_button = Button(text='Copy', size_hint=(None, None), size=(dp(100), dp(40)),
                                 background_color=(0.3, 0.6, 0.9, 1), background_normal='', background_down='')
            copy_button.bind(on_release=lambda btn, address=location['address']: self.copy_address(address))
            delete_button = Button(text='Delete', size_hint=(None, None), size=(dp(100), dp(40)),
                                   background_color=(0.9, 0.3, 0.3, 1), background_normal='', background_down='')
            delete_button.bind(on_release=lambda btn, address=location['address']: self.delete_address(address))
            button_layout.add_widget(copy_button)
            button_layout.add_widget(delete_button)
            layout.add_widget(address_label)
            layout.add_widget(button_layout)

        content_layout = BoxLayout(orientation='vertical')
        content_layout.add_widget(header_layout)
        content_layout.add_widget(layout)

        self.content = content_layout

    def copy_address(self, address):
        pyperclip.copy(address)

    def delete_address(self, address):
        saved_locations = load_saved_locations()
        saved_locations = [location for location in saved_locations if location['address'] != address]
        save_saved_locations(saved_locations)
        self.dismiss()
        ShowSavedLocationsPopup(saved_locations=saved_locations).open()

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        Window.clearcolor = (1, 1, 1, 1)  # Set background color to white

        # Platzhalter für das Logo und die Buttons
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Platzhalter oberhalb der Buttons (nimmt nur den verfügbaren Platz oberhalb des Logos ein)
        layout.add_widget(BoxLayout(size_hint=(1, None), height=(Window.height - dp(200))))


        # Logo hinzufügen (zentriert)
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(300), dp(300)), pos_hint={'center_x': 0.5})
        layout.add_widget(logo)

        # Buttons hinzufügen
        button_grid = self.create_buttons()
        layout.add_widget(button_grid)

        # Platzhalter unterhalb der Buttons (nimmt den verfügbaren Platz unterhalb der Buttons ein)
        layout.add_widget(BoxLayout(size_hint=(1, None), height=(Window.height - logo.height) / 2))



        self.add_widget(layout)



    def create_buttons(self):



        button_grid = GridLayout(cols=1, spacing=20, size_hint_y=None)

        generate_new_button = Button(text='Generate New', size_hint_y=None, height=dp(50),
                                     background_color=(0.3, 0.6, 0.9, 1), background_normal='', background_down='')
        generate_new_button.bind(on_release=self.generate_new)

        saved_locations_button = Button(text='Saved Locations', size_hint_y=None, height=dp(50),
                                        background_color=(0.3, 0.6, 0.9, 1), background_normal='', background_down='')
        saved_locations_button.bind(on_release=self.show_saved_locations)

        info_button_layout = AnchorLayout(anchor_x='right', anchor_y='bottom', size_hint=(None, None),
                                          size=(Window.width-dp(50), dp(110)))
        info_button = Button(background_normal='info.png', background_down='info.png', size_hint=(None, None),
                             size=(dp(40), dp(40)), background_color=(0.3, 0.6, 0.9, 1))

        info_button.bind(on_release=self.info_button_popup)
        info_button_layout.add_widget(info_button)


        button_grid.add_widget(generate_new_button)
        button_grid.add_widget(saved_locations_button)
        button_grid.add_widget(info_button_layout)

        return button_grid

    def generate_new(self, instance):
        self.manager.current = 'map'

    def show_saved_locations(self, instance):
        saved_locations = load_saved_locations()
        if saved_locations:
            saved_locations_popup = ShowSavedLocationsPopup(saved_locations=saved_locations)
            saved_locations_popup.open()
        else:
            no_saved_locations_popup = Popup(title='Saved Locations', content=Label(text="No saved locations found."), size_hint=(None, None), size=(400, 200))
            no_saved_locations_popup.open()

    def info_button_popup(self, instance):
        info_button_popup = Popup(title='Info', content=Label(text="Info"), size_hint=(None, None), size=(400, 200))
        info_button_popup.open()


class MapScreen(Screen):
    def __init__(self, **kwargs):
        super(MapScreen, self).__init__(**kwargs)

        self.map_view = MapWithMarker()
        self.add_widget(self.map_view)


    def go_to_start(self, instance):
        self.manager.current = 'start'


class MyApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MapScreen(name='map'))

        return sm

    def on_pause(self):

        return True
    def on_resume(self):
        pass


def load_saved_locations():
    try:
        with open("saved_locations.json", "r") as file:
            saved_locations = json.load(file)
    except FileNotFoundError:
        saved_locations = []
    return saved_locations


def save_saved_locations(saved_locations):
    with open("saved_locations.json", "w") as file:
        json.dump(saved_locations, file)


if __name__ == '__main__':
    MyApp().run()
