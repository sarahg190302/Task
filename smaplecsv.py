import csv
import random
import string

# Function to generate random name
def generate_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))

# Function to generate random age (between 18 and 60)
def generate_age():
    return random.randint(18, 60)

# Function to generate random ID (6-digit number)
def generate_id():
    return random.randint(100000, 999999)

# Number of records to generate
num_records = 20

# Generate data and write to CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(['name', 'age', 'id'])
    
    # Write records
    for _ in range(num_records):
        name = generate_name()
        age = generate_age()
        id = generate_id()
        writer.writerow([name, age, id])

print("CSV file generated successfully.")
