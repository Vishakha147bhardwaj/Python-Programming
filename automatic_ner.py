import spacy

def extract_marketing_insights(web_copy):
    # Load spaCy pipeline
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(web_copy)
    
    # Custom storage buckets using sets to automatically prevent duplicate entries
    extracted_data = {
        "BRANDS (ORG)": set(),
        "PRODUCTS (PRODUCT)": set(),
        "LOCATIONS (GPE/LOC)": set()
    }
    
    # Filter through the identified entities
    for ent in doc.ents:
        if ent.label_ == "ORG":
            extracted_data["BRANDS (ORG)"].add(ent.text)
        elif ent.label_ == "PRODUCT":
            extracted_data["PRODUCTS (PRODUCT)"].add(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            extracted_data["LOCATIONS (GPE/LOC)"].add(ent.text)
            
    # Print the findings cleanly
    for category, items in extracted_data.items():
        print(f"\n🔹 {category}:")
        if items:
            for item in items:
                print(f"  - {item}")
        else:
            print("  - None found")

# Mock website copy from a tech company homepage
homepage_text = """
Welcome to NextGen Robotics! Headquartered in Tokyo, we manufacture cutting-edge machinery. 
Our flagship system, the AeroDrone X, is now shipping to clients across Germany and France. 
By partnering with Microsoft Azure, we ensure your production facility operates seamlessly.
"""

# Run the automated extraction
extract_marketing_insights(homepage_text)
