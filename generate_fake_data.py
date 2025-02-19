# generate_fake_data.py
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake data
name = fake.name()
address = fake.address()
email = fake.email()

# Print the generated fake data
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Email: {email}")
