import sqlite3
connection = sqlite3.connect("company_store.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")
cursor.execute("""
INSERT INTO employees (name, department, salary) 
VALUES ('Ananya', 'Sales', 60000)
""")

connection.commit()

connection.close()
