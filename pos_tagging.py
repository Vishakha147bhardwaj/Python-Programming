import spacy

# Load the English pipeline
nlp = spacy.load("en_core_web_sm")

text = "Apple is looking at buying a fast startup."

# Process the text through the pipeline
doc = nlp(text)

# Print headers neatly aligned using the :<12 technique
print(f"{'Token':<12} | {'POS Tag':<12} | {'Description':<12}")
print("-" * 45)

# Iterate through every token in the document
for token in doc:
    print(f"{token.text:<12} | {token.pos_:<12} | {spacy.explain(token.pos_)}")
