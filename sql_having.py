import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

# --- THE QUERY ---
# "Group by category, calculate the total sales, but only show me categories where that total is more than $100."
cursor.execute("""
SELECT category, SUM(price)
FROM sales
GROUP BY category
HAVING SUM(price) > 100.00
""")

rows = cursor.fetchall()

print("--- High-Performing Categories (Over $100 Sales) ---")
for row in rows:
    print(f"Top Category: {row[0]} | Total Sales: ${row[1]:.2f}")

connection.close()
