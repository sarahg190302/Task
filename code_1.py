import psycopg2
import json

# Connect to the database
conn = psycopg2.connect(
    dbname="T_2",
    user="postgres",
    password="Sarah1903@",
    host="localhost"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM taskpr")

# Fetch all rows
rows = cur.fetchall()

# Convert rows to dictionary
data = [{'name': row[0], 'age': row[1], 'id': row[2]} for row in rows]

# Convert data to JSON
json_data = json.dumps(data, indent=4)

# Print or save JSON data as required
print(json_data)

# Close communication with the database
cur.close()
conn.close()


# Save JSON data to a file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("JSON data saved to data.json file.")
