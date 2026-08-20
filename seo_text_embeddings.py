from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

# Topics covered on YOUR blog
my_topics = [
    "Advanced Python coding loops",
    "How to install SQL databases"
]

# Topics covered on a COMPETITOR'S blog
competitor_topics = [
    "Introduction to Python programming basics",
    "How to use text embeddings for SEO analysis",  # <-- We missed this entirely!
    "Setting up a PostgreSQL database connection"
]

print("--- Running Content Gap Analysis ---")

# For every topic our competitor wrote about...
for comp_topic in competitor_topics:
    comp_embedding = model.encode([comp_topic])
    
    # Check it against all of our topics to find the highest match
    highest_similarity = 0
    for my_topic in my_topics:
        my_embedding = model.encode([my_topic])
        similarity = cosine_similarity(comp_embedding, my_embedding)[0][0]
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            
    # If the highest similarity score is low, it means we don't cover it!
    # A threshold of 0.5 is standard for detecting completely new topics
    if highest_similarity < 0.50:
        print(f"❌ GAP FOUND! Competitor covers: '{comp_topic}'")
        print(f"   (Your closest piece was only {highest_similarity*100:.1f}% similar)\n")
    else:
        print(f"✅ Covered. Competitor topic: '{comp_topic}' matches your site at {highest_similarity*100:.1f}%\n")
