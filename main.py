# main.py
import importlib
from commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CalculatorApp:
    def __init__(self):
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }
        self.load_plugins()
    
    def load_plugins(self):
        try:
            menu_plugin = importlib.import_module('plugins.menu')  # Dynamically load the menu plugin
            self.show_menu = menu_plugin.show_menu  # Use the show_menu function from the plugin
        except ModuleNotFoundError:
            print("Menu plugin not found.")
    
    def start(self):
        print("Welcome to the interactive calculator!")
        while True:
            command = input("Enter command (add, subtract, multiply, divide) or 'menu' to see available commands: ")
            if command == "menu":
                self.show_menu()
            elif command in self.commands:
                self.execute_command(command)
            elif command == "exit":
                break
            else:
                print("Invalid command, please try again.")
    
    def execute_command(self, command):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = self.commands[command].execute(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.start()
