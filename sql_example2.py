import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE staff (id INTEGER, name TEXT, department TEXT, salary INTEGER)")
employees = [(1, 'Alice', 'HR', 50000), (2, 'Bob', 'IT', 75000), (3, 'Charlie', 'IT', 85000), (4, 'Diana', 'Sales', 60000)]
cursor.executemany("INSERT INTO staff VALUES (?, ?, ?, ?)", employees)

# --- THE QUERY ---
# "Find the names and salaries of staff in IT making over $70,000, sort highest to lowest, and show the top 1."
cursor.execute("""
SELECT name, salary 
FROM staff
WHERE department = 'IT' AND salary > 70000
ORDER BY salary DESC
LIMIT 1
""")

top_earner = cursor.fetchone()

print("--- Advanced Query Output ---")
print(f"The highest paid eligible IT member is {top_earner[0]} making ${top_earner[1]}")

connection.close()
