import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname="T_2",
    user="postgres",
    password="Sarah1903@",
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute('SELECT id FROM taskpr')
records= cur.fetchall()
print(records)

# Update the name column
cur.execute("UPDATE taskpr SET name='abby' WHERE id=2")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()