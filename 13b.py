import sqlite3
import csv
# Connect to SQLite database (or create it if it doesn't exist)
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
# Open the CSV file and import data into the database
with open('employees.csv', 'r') as csv_file:
csv_reader = csv.reader(csv_file)
next(csv_reader) # Skip the header row
for row in csv_reader:
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (row[0], int(row[1])))
# Commit the changes
conn.commit()
# Display all records in the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("All Employees:")
for row in rows:
print(row)
# Close the database connection
conn.close()