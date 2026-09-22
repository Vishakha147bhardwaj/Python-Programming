import yake

text = "Deep learning and neural networks power modern artificial intelligence systems."

# Initialize YAKE! for single-document extraction
kw_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, top=3)
keywords = kw_extractor.extract_keywords(text)

for kw, score in keywords:
    print(f"Keyword: {kw} | Score: {score}")
