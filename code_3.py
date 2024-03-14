import psycopg2
import json

# Connect to the database
conn = psycopg2.connect(
    dbname="T_2",
    user="postgres",
    password="Sarah1903@",
    host="localhost", 
    port="5432"
    )

# Create a cursor object
cur = conn.cursor()

# Delete the existing data
cur.execute("DELETE FROM taskpr WHERE id IN (1, 2, 3)")

# Insert the new data
new_data = [{'name': 'John', 'age': 25, 'id': 1}, {'name': 'Jane', 'age': 22, 'id': 2}, {'name': 'Mike', 'age': 28, 'id': 3}, {'name': 'Emma', 'age': 30, 'id': 4}]
for data in new_data:
    cur.execute("INSERT INTO taskpr (name, age, id) VALUES (%s, %s, %s)", (data['name'], data['age'], data['id']))


# Commit the changes
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()

