import sqlite3

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create the websites table
cursor.execute("""
CREATE TABLE websites (
    website_id INTEGER PRIMARY KEY,
    company_name TEXT,
    domain_url TEXT
);
""")

# Insert data
cursor.executemany("""
INSERT INTO websites VALUES (?, ?, ?)
""", [
    (10, "Nike", "nike.com"),
    (20, "Blue Bottle Coffee", "bluebottle.com"),
    (30, "Local Gym LLC", "localgym.com")
])

# Create the keywords table
cursor.execute("""
CREATE TABLE keywords (
    keyword_id INTEGER PRIMARY KEY,
    keyword_text TEXT,
    google_rank INTEGER,
    website_id INTEGER,
    FOREIGN KEY (website_id) REFERENCES websites(website_id)
);
""")

# Insert data
cursor.executemany("""
INSERT INTO keywords VALUES (?, ?, ?, ?)
""", [
    (101, "air jordan 1 retro", 2, 10),
    (102, "vaporfly running shoes", 5, 10),
    (103, "organic espresso beans", 1, 20)
])

# INNER JOIN
cursor.execute("""
SELECT
    k.keyword_text,
    w.company_name
FROM keywords k
INNER JOIN websites w
ON k.website_id = w.website_id;
""")

print("INNER JOIN")
for row in cursor.fetchall():
    print(row)

# LEFT JOIN
cursor.execute("""
SELECT
    w.company_name,
    k.keyword_text
FROM websites w
LEFT JOIN keywords k
ON w.website_id = k.website_id;
""")

print("\nLEFT JOIN")
for row in cursor.fetchall():
    print(row)

conn.close()