import importlib
import logging
from dotenv import load_dotenv
import os
from commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.INFO,  # Set minimum logging level (e.g., INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
)

# Load environment variables from the .env file
load_dotenv()

# Get environment variables
ENV = os.getenv("ENVIRONMENT")
API_KEY = os.getenv("API_KEY")

# Log the environment variables (for debugging purposes)
logging.info(f"Running in {ENV} mode")
logging.info(f"API Key: {API_KEY}")

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
            # Dynamically load the menu plugin (ensure plugins.menu is present)
            menu_plugin = importlib.import_module('plugins.menu')
            self.show_menu = menu_plugin.show_menu  # Use the show_menu function from the plugin
            logging.info("Menu plugin loaded successfully.")
        except ModuleNotFoundError:
            logging.error("Menu plugin not found.")
            self.show_menu = lambda: "No menu available."  # Default if plugin not found
    
    def start(self):
        logging.info("Starting the interactive calculator.")
        print("Welcome to the interactive calculator!")
        while True:
            command = input("Enter command (add, subtract, multiply, divide) or 'menu' to see available commands: ")
            if command == "menu":
                logging.info("User requested the menu.")
                print(self.show_menu())  # Display the menu when 'menu' is entered
            elif command in self.commands:
                self.execute_command(command)
            elif command == "exit":
                logging.info("User exited the calculator.")
                break
            else:
                logging.warning(f"Invalid command: {command}")
                print("Invalid command, please try again.")
    
    def execute_command(self, command):
        try:
            # Collect inputs for calculation
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            # Execute the command (add, subtract, multiply, divide)
            result = self.commands[command].execute(a, b)
            logging.info(f"Executed command: {command}, Result: {result}")
            print(f"Result: {result}")
        except ValueError as e:
            logging.error(f"Error occurred: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.start()
