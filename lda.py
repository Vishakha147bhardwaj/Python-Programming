from gensim import corpora
from gensim.models import LdaModel

# Step 1: Raw Document Intake
# Imagine these are incoming logs or short descriptions from an engineering repository
documents = [
    "AI models use neural networks for deep machine learning tasks",
    "Data science requires statistical analysis and clean training data",
    "Neural networks power modern artificial intelligence applications"
]

# Step 2: Tokenization
# We lowercase the text and split it into clean individual word strings
tokenized_docs = [doc.lower().split() for doc in documents]

# Step 3: Build the Dictionary Map
# This tracks vocabulary across all documents and gives each word a unique structural index ID
dictionary = corpora.Dictionary(tokenized_docs)

# Step 4: Generate the Bag-of-Words (BoW) Corpus
# Converts words into structured coordinate pairings: (Word_ID, Frequency_Count)
corpus = [dictionary.doc2bow(text) for text in tokenized_docs]

# Step 5: Initialize and Train the LDA Model
# We explicitly direct the engine to seek out exactly 2 distinct hidden topics
lda_model = LdaModel(
    corpus=corpus, 
    id2word=dictionary, 
    num_topics=2, 
    random_state=42,  # Ensures reproducibility across runs
    passes=10         # Number of training loops through the entire corpus
)

# Step 6: Output the Discovered Topics
# Print the most dominant keywords associated with each hidden topic
print("--- Discovered Topic Keyword Clusters ---")
for idx, topic in lda_model.print_topics(num_topics=2, num_words=4):
    print(f"Topic #{idx}: {topic}")
