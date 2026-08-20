import sqlite3

connection = sqlite3.connect("marketing_data.db")  # Use an in-memory database for testing

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS seo_keywords (
    keyword_id INTEGER PRIMARY KEY,
    keyword_text TEXT,
    search_volume INTEGER,
    difficulty_score REAL
)
""")

cursor.execute("INSERT INTO seo_keywords VALUES (101, 'ai marketing tools', 45000, 72.5)")
cursor.execute("INSERT INTO seo_keywords VALUES (102, 'python for beginners', 12000, 34.1)")
cursor.execute("INSERT INTO seo_keywords VALUES (103, 'best autonomous agents', 8500, 88.0)")

connection.commit()

cursor.close()
connection.close()

