"""
This module contains the Calculation class for storing individual calculations.
"""

class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, operation: str, a: float, b: float, result: float):
        """Initializes the Calculation object with operation, operands, and result."""
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __str__(self):
        """Returns a string representation of the calculation."""
        return f"{self.operation}({self.a}, {self.b}) = {self.result}"
