import sqlite3

# --- 1. SET UP SQLITE ---
# This creates a file named 'classroom.db' instantly in your folder
connection = sqlite3.connect("classroom.db")

# Create a 'cursor' (Think of this as the blinking cursor/pointer to type commands)
cursor = connection.cursor()

# --- 2. CREATE A TABLE (With Rows, Columns, & Primary Key) ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade TEXT
)
""")

# --- 3. INSERT DATA ---
# Adding records to our table
cursor.execute("INSERT OR IGNORE INTO students (student_id, name, grade) VALUES (101, 'Alice', 'A')")
cursor.execute("INSERT OR IGNORE INTO students (student_id, name, grade) VALUES (102, 'Bob', 'B')")

# Save our changes to the file
connection.commit()

# --- 4. QUERY THE DATA ---
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print("--- Data Retrieved From SQLite Database ---")
for row in all_students:
    print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]}")

# Close the notebook when done
connection.close()
