import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_multiply():
    assert Calculator.multiply(3, 4) == 12

def test_divide():
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)

def test_operations(generate_test_data):
    for a, b, operation, expected in generate_test_data:
        if operation == "add":
            assert Calculator.add(a, b) == expected
        elif operation == "subtract":
            assert Calculator.subtract(a, b) == expected
        elif operation == "multiply":
            assert Calculator.multiply(a, b) == expected
        elif operation == "divide":
            if b != 0:
                assert Calculator.divide(a, b) == expected
            else:
                with pytest.raises(ValueError):
                    Calculator.divide(a, b)
# test_calculator.py
import pytest

@pytest.fixture
def generate_test_data():
    # Your code to generate fake test data
    return {
        "a": 5,
        "b": 3,
        "operation": "add",
        "expected_result": 8
    }

def test_operations(generate_test_data):
    data = generate_test_data
    # Perform the test using the generated data
    assert data["a"] + data["b"] == data["expected_result"]


