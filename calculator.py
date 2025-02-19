"""
This module contains the Calculator class for performing basic operations.
"""

class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""
    
    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        result = a + b
        Calculator.history.append(("add", a, b, result))
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        result = a - b
        Calculator.history.append(("subtract", a, b, result))
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        result = a * b
        Calculator.history.append(("multiply", a, b, result))
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of two numbers. Raises ValueError if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(("divide", a, b, result))
        return result

    @classmethod
    def get_history(cls):
        """Returns the history of calculations."""
        return cls.history
