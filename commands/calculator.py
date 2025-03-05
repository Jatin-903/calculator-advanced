class AddCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

class SubtractCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

class MultiplyCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b

class DivideCommand:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b
