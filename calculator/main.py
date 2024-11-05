# import gi
# import sys

# gi.require_version("Gtk", "4.0")

# from gi.repository import GLib, Gtk

from tkinter import *
from tkinter import ttk

class IntButton:
    def __init__(self, calculator, name):
        self.calculator = calculator
        self.number = name
        self.button = ttk.Button(calculator.window, text=name, command=self.do_clicked)

    # Called when the button is pressed
    def do_clicked(self):
        self.calculator.handle_digit(self.number)
        print(f"Number button {self.number} pressed")

class SpecialButton:
    def __init__(self, calculator, name):
        self.calculator = calculator
        self.name = name
        self.button = ttk.Button(calculator.window, text=name, command=self.do_clicked)

    # Called when the button is pressed
    def do_clicked(self):
        self.calculator.handle_operation(self.name)
        print(f"special button {self.name} pressed")

class Calculator:
    def __init__(self, root):
        # Initialise registers
        self.disp = 0
        self.stored_op = None

        # Create a new window
        self.window = ttk.Frame(root, padding = 10)
        # Use the grid geometry manager
        self.window.grid()
        # Attach the display to the top of the grid
        self.display = ttk.Label(self.window, text="0")
        self.display.grid(column = 0, row = 0, columnspan=4)
        COLUMNS = 4
        # Create buttons
        for index, button_name in enumerate([
            "0", "1", "2", "3",
            "4", "5", "6", "7",
            "8", "9", "+", "-",
            "*", "/", "%", "=" ]):
            button = self.makeButton(button_name)
            button.button.grid(column = index % COLUMNS, row = index // COLUMNS + 1)
        print("Compsoc calculator")

    # Show the display register
    def redo_display(self):
        # Update display
        self.display["text"] = str(self.disp)

    # Show the accumulator
    def display_acc(self):
        self.display["text"] = str(self.acc)

    # Handle number button press
    def handle_digit(self, digit):
        # Shift disp register left by 1 and add digit
        self.disp = self.disp * 10 + digit
        print(self.disp)
        self.redo_display()

    def handle_operation(self, op):
        # If user has pressed a button previously
        if self.stored_op:
            # Perform operation
            if self.stored_op == "+":
                self.acc = self.acc + self.disp
            elif self.stored_op == "*":
                self.acc = self.acc * self.disp
            elif self.stored_op == "/":
                self.acc = self.acc / self.disp
            elif self.stored_op == "-":
                self.acc = self.acc + self.disp
            elif self.stored_op == "%":
                self.acc = self.acc % self.disp
            elif self.stored_op == "=":
                self.acc = self.disp
            # Clear the display register
            self.disp = 0
            # Show the accumulator
            self.display_acc()
            # Remember the current operation
            self.stored_op = op
        else:
            # Move the display register to the accumulator
            self.acc = self.disp
            # Remember the current operation
            self.stored_op = op
            # Clear the display register
            self.disp = 0
            # Show the display register
            self.redo_display()

    def makeButton(self, name):
        try:
            return IntButton(self, int(name))
        except ValueError:
            return SpecialButton(self, name)

def main():
    # Create calculator
    root = Tk()
    root.title("Compsoc Calculator")
    app = Calculator(root)
    # Run main loop
    root.mainloop()
    print("I LOVE MAX! MAX IS THE GREETEST!")

if __name__ == "__main__":
    main()
