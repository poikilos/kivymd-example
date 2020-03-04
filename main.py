from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

class ContentNavDrawer(ThemableBehavior, MDList):
    pass

class Main(MDApp):

    def __init__(self, **kwargs):
        # self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file("main.kv")

    def imprimir(self, texto):
        self.root.ids.nav_drawer.set_state("toggle")

if __name__ == "__main__":
    Main().run()
