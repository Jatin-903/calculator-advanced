# tests/test_calculator.py

from commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
import pytest

# Add your test functions here
def test_add():
    add_command = AddCommand(1, 2)
    result = add_command.execute()
    assert result == 3

def test_subtract():
    subtract_command = SubtractCommand(5, 3)
    result = subtract_command.execute()
    assert result == 2

def test_multiply():
    multiply_command = MultiplyCommand(4, 3)
    result = multiply_command.execute()
    assert result == 12

def test_divide():
    divide_command = DivideCommand(6, 2)
    result = divide_command.execute()
    assert result == 3
