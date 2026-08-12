import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

# --- THE QUERY ---
# "Sort the items by category. For each category, tell me its name, count its rows, and add up its prices."
cursor.execute("""
SELECT category, COUNT(sale_id), SUM(price)
FROM sales
GROUP BY category
""")
# 0        1     2
# clothing 3     80
# shoes    2     200
rows = cursor.fetchall()

print("--- Sales Breakdown By Category ---")
for row in rows:
    print(f"Category: {row[0]} | Total Items Sold: {row[1]} | Total Category Sales: ${row[2]:.2f}")

connection.close()