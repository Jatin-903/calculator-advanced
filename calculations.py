"""
This module contains the Calculations class to store and manage multiple calculations.
"""

class Calculations:
    """Manages a history of calculations."""
    
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        """Adds a calculation object to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """Returns the last calculation in the history, or None if empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls):
        """Returns the complete history of calculations."""
        return cls.history
