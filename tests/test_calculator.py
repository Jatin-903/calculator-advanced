# tests/test_calculator.py
from calculator_project.commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


def test_add():
    add = AddCommand()
    assert add.execute(1, 2) == 3

def test_subtract():
    subtract = SubtractCommand()
    assert subtract.execute(5, 3) == 2

def test_multiply():
    multiply = MultiplyCommand()
    assert multiply.execute(3, 2) == 6

def test_divide():
    divide = DivideCommand()
    assert divide.execute(6, 2) == 3
    try:
        divide.execute(1, 0)
    except ValueError:
        pass
