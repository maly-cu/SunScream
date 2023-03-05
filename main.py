from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.utils import platform
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class LandingPage(Screen):
    pass


class HomePage(Screen):
    pass


class ActivePage(Screen):
    set_temp = 32
    uvi = 0

    temp_text = f"[b]{set_temp}°C[/b]\n[size=12dp]UVI: {uvi}[/size]"  # edit text with diff sizes in same label

    # temp_text = f"{set_temp}°C"
    # uvi_text = f"UVI: {uvi}"

    bar_width = 10
    bar_color = ListProperty([1, 1, 0])


class AboutPage(Screen):
    # def __init__(self, **kwargs):
    #     super(AboutPage, self).__init__(**kwargs)
    #
    with open("about.txt") as f:
        contents = f.read()


class Navigator(ScreenManager):
    pass


# ALWAYS do this just BEFORE MAIN APP class, else it loads first without declaring classes above
kv = Builder.load_file("my.kv")


class MyMainApp(App):
    # Configure phone gps & phone permission
    def configure_gps(self):

        # Request permissions on Android using android module
        if platform == 'android':
            from android.permissions import Permission, request_permissions

            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                else:
                    print("Didn't get all permissions")

            request_permissions([Permission.INTERNET, Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)
        # Configure gps
        if platform == 'android' or platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.get_location,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)

    # called and assigned the location from phone gps. Will use to get weather info
    def get_location(self, *args, **kwargs):
        current_lat = kwargs['lat']
        current_lon = kwargs['lon']
        print('GPS POSITION, ', current_lat, current_lon)

    # checks the status of authorisation
    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    # Popup to tell you to turn on location for app
    def open_gps_access_popup(self):
        dialog =MDDialog(
                title="GPS Error",
                text="App needs Location enabled to function properly",
        )
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()

    def build(self):
        # Change window color
        if platform not in ["android", "ios"]:
            Window.size = (320, 640)
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == "__main__":
    MyMainApp().run()