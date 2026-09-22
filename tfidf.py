from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "Deep learning and neural networks power modern artificial intelligence.",
    "Artificial intelligence models require massive data and deep compute layers.",
    "Neural networks mimic the biological structure of the human brain."
]

# Initialize vectorizer with n-grams (unigrams and bigrams)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(corpus)

# Extract feature names and scores for the first document
feature_names = vectorizer.get_feature_names_out()
first_doc_scores = tfidf_matrix.toarray()[0]

# Pair and sort keywords by weight
keywords = sorted(zip(feature_names, first_doc_scores), key=lambda x: x[1], reverse=True)
print(keywords[:3])
# Output might show: [('modern artificial', 0.43), ('neural networks', 0.31), ('deep learning', 0.31)]
