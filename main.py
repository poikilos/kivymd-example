from kivymd.app import MDApp
from kivymd.theming import ThemeManager


class Main(MDApp):
    theme_cls = ThemeManager()

    def open_menu(self, widget):
        self.root.toggle_nav_drawer()

    def imprimir(self, texto):
        print(texto)

if __name__ == "__main__":
    Main().run()
