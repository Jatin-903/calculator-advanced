import pytest
from faker import Faker
fake = Faker()

@pytest.fixture(scope='session')
def fake_data(request):
    num_records = request.config.getoption("--num_records", default=10, type=int)
    data = []
    for _ in range(num_records):
        record = {
            "a": fake.random_number(),
            "b": fake.random_number(),
            "operation": fake.random_element(elements=('add', 'subtract', 'multiply', 'divide')),
            "expected_result": fake.random_number()
        }
        data.append(record)
    return data

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int)
import pytest
from faker import Faker

fake = Faker()

# Fixture to generate fake data for testing
@pytest.fixture
def generate_test_data():
    data = {
        "a": fake.random_number(),
        "b": fake.random_number(),
        "operation": fake.random_element(elements=("add", "subtract", "multiply", "divide")),
        "expected_result": fake.random_number(),
    }
    return data
