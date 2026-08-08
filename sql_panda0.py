import sqlite3

# 1. Establish the connection line (creates a file called agency.db)
connection = sqlite3.connect("agency.db")

# 2. Spawn our cursor worker robot
cursor = connection.cursor()

# 3. Give the instruction to create a brand new table
cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing_targets (
    target_id INTEGER PRIMARY KEY,
    keyword_text TEXT,
    monthly_volume INTEGER
)
""")

# 4. Give the instruction to insert a client keyword row
cursor.execute("""
INSERT INTO marketing_targets (target_id, keyword_text, monthly_volume) 
VALUES (1, 'best running shoes', 5000)
""")

# 5. Hit the permanent save button
connection.commit()

# 6. Hang up the digital phone line
connection.close()

print("Database initialized and keyword saved successfully!")
