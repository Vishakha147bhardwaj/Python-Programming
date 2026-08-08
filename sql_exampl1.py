import sqlite3

# Connect and setup an in-memory temporary staff database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE staff (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

employees = [
    (1, 'Alice', 'HR', 50000),
    (2, 'Bob', 'IT', 75000),
    (3, 'Charlie', 'IT', 85000),
    (4, 'Diana', 'Sales', 60000)
]
cursor.executemany("INSERT INTO staff VALUES (?, ?, ?, ?)", employees)
connection.commit()

# --- THE QUERY ---
# "Hey database, give me just the name and department columns from the staff table."
cursor.execute("""
SELECT name, department 
FROM staff
""")

results = cursor.fetchall()
# results = name  department
        #  'Alice'.  HR
        #  'Bob'     IT
        #  'Charlie' Sales
        #  'Diana'   HR
print("--- Simple Select Output ---")
for row in results:
    print(f"Employee: {row[0]} works in {row[1]}")

connection.close()
 
 