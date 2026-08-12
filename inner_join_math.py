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

# Insert sample keyword data
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
    clicks INTEGER,
    FOREIGN KEY (keyword_id) REFERENCES keywords(keyword_id)
);
""")

# Insert ranking data
cursor.executemany("""
INSERT INTO rankings VALUES (?, ?, ?, ?)
""", [
    (1, 101, 3, 18000),
    (2, 102, 12, 4500),
    (3, 103, 7, 5000),
    (4, 104, 1, 25000)
])

# ---------------------------------------------------------
# STEP 4: Find Top-10 Ranking Keywords and Calculate CTR
# ---------------------------------------------------------
cursor.execute("""
SELECT
    keywords.keyword_text,
    rankings.google_position,
    (rankings.clicks * 100.0 / keywords.search_volume) AS click_rate
FROM keywords
INNER JOIN rankings
ON keywords.keyword_id = rankings.keyword_id
WHERE rankings.google_position <= 10;
""")
# keyword_text         google_position   click_rate
# air jordan 1 retro     3                 15.00
# organic espresso beans   7                 20.00
# home workout equipment   1                 41.67

# ---------------------------------------------------------
# STEP 5: Display the Results
# ---------------------------------------------------------
print("=== Top 10 Ranking Keywords ===")
print("-" * 65)
# results = cursor.fetchall()
for keyword, position, click_rate in cursor.fetchall():
    print(f"Keyword         : {keyword}")
    print(f"Google Position : {position}")
    print(f"Click Rate      : {click_rate:.2f}%")
    print("-" * 65)

# Close the database
conn.close()