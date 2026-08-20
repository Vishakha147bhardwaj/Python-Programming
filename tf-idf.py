from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 1. Create a mini library of 3 sample documents
library = [
    "The pizza was delicious with lots of cheese and pepperoni toppings.",
    "Python is a great programming language for data analysis and software.",
    "To make great pizza you need high quality cheese and fresh dough."
]

# 2. Initialize the TF-IDF engine
vectorizer = TfidfVectorizer()

# 3. Let the engine read the library and calculate the math
tfidf_matrix = vectorizer.fit_transform(library)

# 4. Convert the math into a readable table
word_features = vectorizer.get_feature_names_out()
df = pd.DataFrame(tfidf_matrix.toarray(), columns=word_features)

# Let's see the scores for Document 0 (The first text)
print(df.iloc[0].sort_values(ascending=False))
