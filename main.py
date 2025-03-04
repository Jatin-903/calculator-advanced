import importlib
from commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CalculatorApp:
    def __init__(self):
        # Commands dictionary with the respective classes (without parameters)
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }
        self.load_plugins()
    
    def load_plugins(self):
        try:
            # Dynamically load the menu plugin
            menu_plugin = importlib.import_module('plugins.menu')
            self.show_menu = menu_plugin.show_menu  # Use the show_menu function from the plugin
        except ModuleNotFoundError:
            print("Menu plugin not found.")
    
    def start(self):
        print("Welcome to the interactive calculator!")
        while True:
            command = input("Enter command (add, subtract, multiply, divide) or 'menu' to see available commands: ")
            if command == "menu":
                print(self.show_menu())  # Display the menu when 'menu' is entered
            elif command in self.commands:
                self.execute_command(command)
            elif command == "exit":
                break
            else:
                print("Invalid command, please try again.")
    
    def execute_command(self, command):
        try:
            # Collect inputs for calculation
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            # Execute the command (add, subtract, multiply, divide)
            result = self.commands[command].execute(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.start()
