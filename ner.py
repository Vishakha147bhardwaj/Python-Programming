import spacy

nlp = spacy.load("en_core_web_sm")
text = "Google released the Pixel 8 phone in Paris last October."

doc = nlp(text)

# Access entities directly using doc.ents
for ent in doc.ents:
    print(f"Entity: {ent.text:<18} | Label: {ent.label_:<10} | Meaning: {spacy.explain(ent.label_)}")
