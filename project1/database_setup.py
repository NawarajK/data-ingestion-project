import sqlite3
# for connecting with SQLite database
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()
# creating a table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers(
               id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, country TEXT)
               ''')

# this is sample data inserted into the database
sample_customers = [
    ('Alice', 28, 'UK'),
    ('Bob', 35, 'USA'),
    ('Charlie', 33, 'India')
]

cursor.executemany(
    'INSERT INTO customers (name, age, country) VALUES (?,?, ?)', sample_customers
)
conn.commit()
conn.close()
print("Database and table created successfully!")
