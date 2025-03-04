# Command classes for calculator operations
class AddCommand:
    def execute(self, a, b):
        return a + b

class SubtractCommand:
    def execute(self, a, b):
        return a - b

class MultiplyCommand:
    def execute(self, a, b):
        return a * b

class DivideCommand:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
