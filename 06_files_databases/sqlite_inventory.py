import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

name = input("Product: ")
quantity = int(input("Quantity: "))

cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
connection.commit()

for row in cursor.execute("SELECT * FROM products"):
    print(row)

connection.close()
