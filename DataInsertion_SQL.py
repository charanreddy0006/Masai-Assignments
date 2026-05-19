import sqlite3
import pandas as pd

# Create database connection
connection = sqlite3.connect('ecommerce.db')
cursor = connection.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

# Create customers table with constraints
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
""")

# Create orders table with foreign key constraint
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        order_date DATE NOT NULL,
        FOREIGN KEY (customer_id)
            REFERENCES customers(customer_id)
    )
""")

# Sample customer data
customers_data = [
    ("Alice Johnson", "New York"),
    ("Bob Smith", "Chicago"),
    ("Charlie Brown", "New York")
]

# Insert customer data using executemany()
cursor.executemany("""
    INSERT INTO customers (name, city)
    VALUES (?, ?)
""", customers_data)

# Sample order data
orders_data = [
    (1, 150.75, "2026-05-10"),
    (1, 80.50, "2026-05-12"),
    (2, 200.00, "2026-05-11"),
    (3, 120.25, "2026-05-13")
]

# Insert order data using executemany()
cursor.executemany("""
    INSERT INTO orders (customer_id, amount, order_date)
    VALUES (?, ?, ?)
""", orders_data)

# Commit inserted data
connection.commit()

# Query customers from New York with orders over $100
query = """
    SELECT customers.name,
           customers.city,
           orders.amount
    FROM customers
    INNER JOIN orders
        ON customers.customer_id = orders.customer_id
    WHERE customers.city = 'New York'
      AND orders.amount > 100
"""

# Load query results into a Pandas DataFrame
df_results = pd.read_sql_query(query, connection)

# Close the database connection
connection.close()

# Display results
if __name__ == "__main__":
    print(df_results)