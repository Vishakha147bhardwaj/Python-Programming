import spacy

# 1. Load the English language "brain" model
nlp = spacy.load("en_core_web_sm")

# 2. Feed raw text into the spaCy assembly line
text = "Apple released the new iPhone 17 in San Francisco today."
doc = nlp(text)

print("--- PART OF SPEECH (POS) TAGGING ---")
# Loop through every single word token
for token in doc:
    # token.text is the word, token.pos_ is the grammatical tag
    print(f"Word: {token.text:<15} | Grammar Role: {token.pos_}")

print("\n--- NAMED ENTITY RECOGNITION (NER) ---")
# Loop through the detected entities found by the highlighter
for ent in doc.ents:
    # ent.text is the found phrase, ent.label_ is what it is
    print(f"Found Entity: {ent.text:<15} | Category Type: {ent.label_}")
