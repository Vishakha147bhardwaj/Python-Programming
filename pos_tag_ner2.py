import spacy

nlp = spacy.load("en_core_web_sm")

# Real-world messy web copy text
web_copy = """
At Nike, we are scaling our retail footprints across Europe, specifically targeting Paris and Berlin. 
Our latest Air Max sneakers are driving 40% of online conversions. Meanwhile, Adidas is struggling 
to compete with us in Germany, despite lowering prices on their Ultraboost shoes in 2026.
"""

doc = nlp(web_copy)

# Create empty "buckets" to store our marketing intelligence data
extracted_brands = []
extracted_products = []
extracted_locations = []

# Scan the text with our AI highlighter
for ent in doc.ents:
    if ent.label_ == "ORG":         # Companies / Brands
        extracted_brands.append(ent.text)
    elif ent.label_ == "PRODUCT":     # Physical items
        extracted_products.append(ent.text)
    elif ent.label_ == "GPE":         # Geopolitical Entity (Countries/Cities)
        extracted_locations.append(ent.text)

# Print the results cleanly
print("🎯 COMPETITOR INTELLIGENCE REPORT 🎯\n")
print(f"Identified Brands:   {set(extracted_brands)}")
print(f"Tracked Products:    {set(extracted_products)}")
print(f"Key Market Targets:  {set(extracted_locations)}")

# import spacy

# nlp = spacy.load("en_core_web_sm")

# web_copy = """
# At Nike, we are scaling our retail footprints across Europe, specifically targeting Paris and Berlin. 
# Our latest Air Max sneakers are driving 40% of online conversions. Meanwhile, Adidas is struggling 
# to compete with us in Germany, despite lowering prices on their Ultraboost shoes in 2026.
# """

# doc = nlp(web_copy)

# # Our own marketing intelligence dictionary
# known_brands = {
#     "Nike",
#     "Adidas"
# }

# known_products = {
#     "Air Max",
#     "Ultraboost"
# }

# extracted_brands = []
# extracted_products = []
# extracted_locations = []

# # spaCy entities
# for ent in doc.ents:

#     if ent.label_ == "GPE":
#         extracted_locations.append(ent.text)

# # Search specifically for known brands
# for brand in known_brands:
#     if brand.lower() in web_copy.lower():
#         extracted_brands.append(brand)

# # Search specifically for known products
# for product in known_products:
#     if product.lower() in web_copy.lower():
#         extracted_products.append(product)

# print("🎯 COMPETITOR INTELLIGENCE REPORT 🎯\n")

# print(f"Identified Brands:   {set(extracted_brands)}")
# print(f"Tracked Products:    {set(extracted_products)}")
# print(f"Key Market Targets:  {set(extracted_locations)}")