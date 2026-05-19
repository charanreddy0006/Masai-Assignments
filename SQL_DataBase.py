import sqlite3

def create_retail_database():
    with sqlite3.connect('retail.db') as connection:
        # Enable foreign key support
        connection.execute("PRAGMA foreign_keys = ON")

        # Create customers table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                city TEXT
            )
        """)

        # Create orders table with foreign key
        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_date DATE,
                total_amount REAL,
                FOREIGN KEY (customer_id)
                    REFERENCES customers(customer_id)
            )
        """)

        # Commit changes
        connection.commit()

    print("Tables created successfully.")

if __name__ == "__main__":
    create_retail_database()