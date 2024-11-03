import gi
import sys

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk

class IntButton(Gtk.Button):
    def __init__(self, calculator, name):
        self.number = name
        self.calculator = calculator
        super().__init__()
        self.props.label = str(name)

    def do_clicked(self):
        self.calculator.handle_digit(self.number)
        print(f"Number button {self.number} pressed")

class SpecialButton(Gtk.Button):
    def __init__(self, calculator, name):
        self.name = name
        self.calculator = calculator
        super().__init__()
        self.props.label = name

    def do_clicked(self):
        self.calculator.handle_operation(self.name)
        print(f"special button {self.name} pressed")

class Calculator(Gtk.Application):
    def __init__(self):
        super().__init__(application_id = "io.compsoc.calculator")
        self.disp = 0
        GLib.set_application_name("Compsoc calculator")
        self.stored_op = None
        print("Compsoc calculator")

    def redo_display(self):
        self.display.props.label = str(self.disp)

    def display_acc(self):
        self.display.props.label = str(self.acc)

    def handle_digit(self, digit):
        self.disp = self.disp * 10 + digit
        print(self.disp)
        self.redo_display()

    def handle_operation(self, op):
        if self.stored_op:
            if self.stored_op == "+":
                self.acc = self.acc + self.disp
            elif self.stored_op == "*":
                self.acc = self.acc * self.disp
            elif self.stored_op == "/":
                self.acc = self.acc / self.disp
            elif self.stored_op == "-":
                self.acc = self.acc + self.disp
            self.disp = 0
            self.display_acc()
            self.stored_op = op
        else:
            self.acc = self.disp
            self.stored_op = op
            self.disp = 0
            self.redo_display()

    def makeButton(self, name):
        try:
            return IntButton(self, int(name))
        except ValueError:
            return SpecialButton(self, name)

    def do_activate(self):
        window = Gtk.ApplicationWindow(application = self, title = "Compsoc Calculator")
        buttons = {}
        buttonGrid = Gtk.Grid()
        self.display = Gtk.Label.new(str = "0")
        buttonGrid.attach(self.display, 0, 0, 4, 1)
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
