import gi
import sys

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk

class IntButton(Gtk.Button):
    def __init__(self, name):
        super().__init__()
        self.props.label = name

class SpecialButton(Gtk.Button):
    def __init__(self, name):
        super().__init__()
        self.props.label = name

class Calculator(Gtk.Application):
    def __init__(self):
        super().__init__(application_id = "io.compsoc.calculator")
        GLib.set_application_name("Compsoc calculator")
        print("Compsoc calculator")

    @staticmethod
    def makeButton(name):
        if name in map(int, range(0, 9)):
            return IntButton(int(name))
        else:
            return SpecialButton(name)

    def do_activate(self):
        window = Gtk.ApplicationWindow(application = self, title = "Compsoc Calculator")
        buttons = {}
        buttonGrid = Gtk.Grid()
        display = Gtk.Label.new(str = "0")
        buttonGrid.attach(display, 0, 0, 4, 1)
        for index, button_name in enumerate([
            "0", "1", "2", "3",
            "4", "5", "6", "7",
            "8", "9", "+", "-",
            "*", "/" ]):
            # button = Gtk.Button()
            # button.props.child = Gtk.Label.new(str = button_name)
            button = self.makeButton(button_name)
            buttonGrid.attach(button, index % 4, index / 4 + 1, 1, 1)
        window.props.child = buttonGrid
        window.set_resizable = False
        window.present()

def main():
    app = Calculator()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
