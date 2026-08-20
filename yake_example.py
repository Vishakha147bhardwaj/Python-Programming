import yake

# 1. A single standalone text block
text = """
Artificial Intelligence is changing the world. Artificial Intelligence helps 
automate tedious tasks. Many industries are adopting Intelligence systems 
to stay competitive in the modern global market.
"""

# 2. Configure the YAKE tool
# lan="en" (English), n-grams=2 (Look for phrases up to 2 words long)
kw_extractor = yake.KeywordExtractor(lan="en", n=2, top=3)

# 3. Extract the keywords
keywords = kw_extractor.extract_keywords(text)

# 4. Print results (Warning: In YAKE, a LOWER score means MORE important!)
for word, score in keywords:
    print(f"Keyword: {word} | Score: {score:.4f}")
