import sqlite3
# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# Create a table (if not already exists)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
''')
# Insert data into the table
cursor.execute("INSERT INTO employees (name, age) VALUES ('John Doe', 28)")
cursor.execute("INSERT INTO employees (name, age) VALUES ('Jane Smith', 34)")
conn.commit()
# Delete data from the table (e.g., delete the employee with name 'John Doe')
cursor.execute("DELETE FROM employees WHERE name = 'John Doe'")
conn.commit()
# Display all records in the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("All Employees:")
for row in rows:
print(row)
# Close the database connection
conn.close()