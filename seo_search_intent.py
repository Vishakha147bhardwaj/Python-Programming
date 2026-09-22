from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Labeled Training Dataset
training_queries = [
    # Informational
    ("how to implement quicksort in c++", "informational"),
    ("what is the weather today in delhi", "informational"),
    ("python data science tutorial for beginners", "informational"),
    ("guide to fixing error 404", "informational"),
    
    # Transactional
    ("buy iphone 15 pro max online", "transactional"),
    ("cheap flight tickets to london", "transactional"),
    ("download spotify desktop app premium", "transactional"),
    ("nike running shoes discount price", "transactional"),
    
    # Navigational
    ("facebook login page", "navigational"),
    ("youtube dashboard", "navigational"),
    ("gmail sign in portal", "navigational"),
    ("hugging face official website", "navigational")
]

# Separate features (X) and target labels (y)
X_train, y_train = zip(*training_queries)

# 2. Build Pipeline: Text Vectorization -> Classification Model
intent_classifier = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
    ('clf', LogisticRegression(C=1.0, random_state=42))
])

# Train the intent model
intent_classifier.fit(X_train, y_train)

# 3. Real-world Operational Test Inference
unseen_test_queries = [
    "chatgpt official login",
    "where can I buy cheap mechanical keyboards",
    "explanation of transformer multi-head attention mechanism"
]

print("\n--- SEARCH INTENT CLASSIFICATION PREDICTIONS ---")
predictions = intent_classifier.predict(unseen_test_queries)
probabilities = intent_classifier.predict_proba(unseen_test_queries)

for query, prediction, proba in zip(unseen_test_queries, predictions, probabilities):
    max_confidence = max(proba) * 100
    print(f"\nQuery: \"{query}\"")
    print(f"Predicted Intent: **{prediction.upper()}** (Confidence: {max_confidence:.2f}%)")
