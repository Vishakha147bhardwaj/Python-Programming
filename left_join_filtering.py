import sqlite3

# ---------------------------------------------------------
# STEP 1: Create an in-memory database
# ---------------------------------------------------------
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# ---------------------------------------------------------
# STEP 2: Create the keywords table
# ---------------------------------------------------------
cursor.execute("""
CREATE TABLE keywords (
    keyword_id INTEGER PRIMARY KEY,
    keyword_text TEXT,
    search_volume INTEGER
);
""")

# Insert sample keywords
cursor.executemany("""
INSERT INTO keywords VALUES (?, ?, ?)
""", [
    (101, "air jordan 1 retro", 120000),
    (102, "vaporfly running shoes", 85000),
    (103, "organic espresso beans", 25000),
    (104, "home workout equipment", 60000)
])

# ---------------------------------------------------------
# STEP 3: Create the rankings table
# ---------------------------------------------------------
cursor.execute("""
CREATE TABLE rankings (
    ranking_id INTEGER PRIMARY KEY,
    keyword_id INTEGER,
    google_position INTEGER,
    FOREIGN KEY (keyword_id) REFERENCES keywords(keyword_id)
);
""")

# Insert ranking data
# Notice: Keywords 102 and 104 have NO ranking.
cursor.executemany("""
INSERT INTO rankings VALUES (?, ?, ?)
""", [
    (1, 101, 3),
    (2, 103, 8)
])


# ---------------------------------------------------------
# STEP 4: LEFT JOIN to find keywords without rankings
# ---------------------------------------------------------
cursor.execute("""
SELECT
    keywords.keyword_text,
    keywords.search_volume
FROM keywords
LEFT JOIN rankings
ON keywords.keyword_id = rankings.keyword_id
WHERE rankings.google_position IS NULL;
""")
#    (101, "air jordan 1 retro", 120000,1,3),
#     (102, "vaporfly running shoes", 85000,NULL,NULL),
#     (103, "organic espresso beans", 25000,2,8),
#     (104, "home workout equipment", 60000,NULL,NULL)
# ( "vaporfly running shoes", 85000),
# ( "home workout equipment", 60000)
# ---------------------------------------------------------
# STEP 5: Display the results
# ---------------------------------------------------------
print("=== Keywords Without Google Rankings ===")

for keyword, volume in cursor.fetchall():
    print(f"Keyword: {keyword}")
    print(f"Search Volume: {volume}")
    print("-" * 40)

# Close the connection
conn.close()
