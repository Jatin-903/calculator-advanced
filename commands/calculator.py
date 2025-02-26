# commands/calculator.py

class Command:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses should implement this!")

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
