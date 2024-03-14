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

# Execute a SQL query to fetch the data from the table
cur.execute("SELECT * FROM taskpr ORDER BY name ASC")

# Fetch the sorted data as a list of dictionaries
rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]  # Extract column names
sorted_data = [dict(zip(columns, row)) for row in rows]

# Save the sorted data to a new JSON file with a different name
with open('sorted_data.json', 'w') as f:
    json.dump(sorted_data, f, indent=4)

# Print the saved JSON data
print(json.dumps(sorted_data, indent=4))

# Close the cursor and the connection
cur.close()
conn.close()