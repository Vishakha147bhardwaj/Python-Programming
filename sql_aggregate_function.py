import sqlite3

# Connect and setup database
connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    item TEXT,
    category TEXT,
    price REAL
)
""")

# Insert dummy data (Clear existing first to avoid duplicate errors on rerun)
cursor.execute("DELETE FROM sales")
orders = [
    (1, 'T-Shirt', 'Clothing', 20.00),
    (2, 'Jeans', 'Clothing', 50.00),
    (3, 'Sneakers', 'Shoes', 80.00),
    (4, 'Socks', 'Clothing', 10.00),
    (5, 'Boots', 'Shoes', 120.00)
]
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", orders)
connection.commit()

# --- THE QUERY ---
# We want total items sold, total money made, average price, cheapest, and most expensive item.
cursor.execute("""
SELECT 
    COUNT(sale_id), 
    SUM(price), 
    AVG(price), 
    MIN(price), 
    MAX(price) 
FROM sales
""")

result = cursor.fetchone()

print("--- Shop Global Statistics ---")
print(f"Total Items Sold: {result[0]}")
print(f"Total Revenue: ${result[1]:.2f}")
print(f"Average Item Price: ${result[2]:.2f}")
print(f"Cheapest Item: ${result[3]:.2f}")
print(f"Most Expensive Item: ${result[4]:.2f}")

connection.close()
