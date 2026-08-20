def classify_search_intent(query):
    query = query.lower().strip()
    
    # Define indicator keyword buckets
    informational_words = ['how', 'why', 'what is', 'guide', 'tutorial', 'tips', 'learn']
    transactional_words = ['buy', 'price', 'cheap', 'discount', 'coupon', 'shipping', 'store']
    navigational_words = ['login', 'sign in', 'official website', 'homepage', 'portal']
    
    # Check for matches
    if any(word in query for word in transactional_words):
        return "💰 Transactional (User wants to buy)"
    elif any(word in query for word in informational_words):
        return "📚 Informational (User wants to learn)"
    elif any(word in query for word in navigational_words):
        return "🧭 Navigational (User wants to go somewhere)"
    else:
        return "🤷 Unknown / General Interest"

# Testing our classifier with a list of search queries
search_log = [
    "how to bake sourdough bread at home",
    "nike running shoes discount store",
    "facebook login portal link",
    "best running shoes for flat feet"
]

print("--- Running Search Intent Analysis ---")
for search in search_log:
    intent = classify_search_intent(search)
    print(f"Query: '{search}' ──► Intent: {intent}")
