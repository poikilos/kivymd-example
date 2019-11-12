from kivy.app import App
from kivymd.theming import ThemeManager


class Main(App):
    theme_cls = ThemeManager()

    def open_menu(self, widget):
        self.root.toggle_nav_drawer()

    def imprimir(self, texto):
        print(texto)

Main().run()