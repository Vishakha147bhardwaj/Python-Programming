# 1. Build a Pure Python Sentence Tokeniser
# The Challenge:
# Do not use NLTK, spaCy, or regular expressions that just split on periods. Write a function split_sentences(text: str) -> list[str] that correctly identifies sentence boundaries.
# Edge cases to handle:
# • Periods used in abbreviations like Mr., Dr., e.g., or Inc. should not split a sentence.
# • Sentences can end with !, ?, or . followed by quotation marks (e.g., He said, "No!" Then he left.).

def split_sentences(text: str) -> list[str]:
    # Common abbreviations that shouldn't end a sentence
    abbreviations = {"mr.", "mrs.", "dr.", "ms.", "inc.", "co.", "e.g.", "i.e.", "vs."}
    
    sentences = []
    current_sentence = []
    words = text.split()
    
    for i, word in enumerate(words):
        current_sentence.append(word)
        clean_word = word.lower().strip('"\'()[]{}')
        
        # Check if the word ends with sentence-terminating punctuation
        if word[-1] in {'.', '!', '?'} or (len(word) > 1 and word[-2] in {'.', '!', '?'} and word[-1] in {'"', "'"}):
            # If it's a known abbreviation, do not split
            if clean_word in abbreviations:
                continue
            
            # Additional check: If the next word starts with a lowercase letter, it's likely not a new sentence
            if i + 1 < len(words) and words[i+1][0].islower():
                continue
                
            # End of sentence reached
            sentences.append(" ".join(current_sentence))
            current_sentence = []
            
    if current_sentence:
        sentences.append(" ".join(current_sentence))
        
    return sentences

# --- Test ---
text_data = 'Dr. Smith said, "No!" to the plan. Then he left Inc. companies behind.'
print("Question 1 Output:\n", split_sentences(text_data))

# 2. Pandas Text-Cleaning Pipeline for DataFrames
# The Challenge:
# In real-world data science, text comes in large tabular datasets. Write a Python script that takes a Pandas DataFrame containing raw, noisy tweets and creates a clean text column.
# Requirements:
# 1. Lowercase all text.
# 2. Remove Twitter handles (e.g., @JohnDoe).
# 3. Remove hyperlinks (e.g., https://t.co).
# 4. Remove standard punctuation and emojis.
# 5. Filter out empty rows or rows that become empty after cleaning.

import pandas as pd
import re

def clean_tweet_pipeline(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    # Work on a copy to avoid SettingWithCopyWarning
    df = df.copy()
    
    # 1. Lowercase
    df['clean_text'] = df[text_column].str.lower()
    
    # 2. Remove URLs (http/https/ftp)
    df['clean_text'] = df['clean_text'].apply(lambda x: re.sub(r'https?://\S+|www\.\S+', '', str(x)))
    
    # 3. Remove Twitter handles (@username)
    df['clean_text'] = df['clean_text'].apply(lambda x: re.sub(r'@\w+', '', x))
    
    # 4. Remove punctuation, special characters, and non-ASCII emojis
    df['clean_text'] = df['clean_text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['clean_text'] = df['clean_text'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
    
    # 5. Drop rows where text became empty strings or NaN
    df = df[df['clean_text'].str.strip() != '']
    df = df.dropna(subset=['clean_text'])
    
    return df

# --- Test ---
tweets = pd.DataFrame({
    'tweets': [
        "Loving this weather! 😍 Check it out @JohnDoe https://t.co",
        "     ",  # Noisy empty row
        "Just regular text without links."
    ]
})
print("\nQuestion 2 Output:\n", clean_tweet_pipeline(tweets, 'tweets'))

# 3. Word Lemmatiser with Automatic POS Tagging
# The Challenge:
# NLTK's WordNetLemmatizer defaults to treating every word as a noun unless you explicitly pass a Part-of-Speech (POS) tag. Because of this, "running" stays "running" instead of becoming "run".
# Write a function smart_lemmatizer(text: str) -> list[str] that:
# 1. Tokenises the input sentence.
# 2. Dynamically finds the POS tag for each token using nltk.pos_tag.
# 3. Converts NLTK tags to WordNet tags (Noun, Verb, Adjective, Adverb).
# 4. Returns the perfectly lemmatised root words.

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Ensure required resources are downloaded
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)

def get_wordnet_pos(nltk_tag: str) -> str:
    # Map NLTK POS tags to WordNet POS constants
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default fallback

def smart_lemmatizer(text: str) -> list[str]:
    tokens = word_tokenize(text)
    # Get (word, tag) tuples
    pos_tags = nltk.pos_tag(tokens)
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    
    for word, tag in pos_tags:
        wn_tag = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos=wn_tag)
        lemmatized_tokens.append(lemma)
        
    return lemmatized_tokens

# --- Test ---
sentence = "The running cats were jumping quickly and showing their sharpest claws."
print("\nQuestion 3 Output:\n", smart_lemmatizer(sentence))

# 4. Custom N-Gram Tokeniser
# The Challenge:
# Sometimes single words (unigrams) lose context. For instance, "not guilty" means the opposite of "guilty". Write a function generate_ngrams(text: str, n: int) -> list[str] from scratch.
# Requirements:
# 1. Preprocess the text (lowercase, remove punctuation).
# 2. Tokenise by words.
# 3. Generate a list of strings representing sequential tokens of size n (e.g., Bigrams if n=2, Trigrams if n=3).
# • Sample Input: "Machine learning is fun" with n=2
# • Expected Output: ['machine learning', 'learning is', 'is fun']

import string

def generate_ngrams(text: str, n: int) -> list[str]:
    # 1. Preprocess: Lowercase and strip out punctuation
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    
    # 2. Tokenise by whitespace
    tokens = clean_text.split()
    
    # 3. Generate N-grams using a sliding window zip configuration
    if len(tokens) < n:
        return [] # Return empty list if window size exceeds input token count
        
    ngrams = []
    for i in range(len(tokens) - n + 1): 
        ngram_group = tokens[i:i+n]
        ngrams.append(" ".join(ngram_group))
        
    return ngrams

# --- Test ---
sample_phrase = "Machine learning is fun, right?"
print("\nQuestion 4 Output (Bigrams):\n", generate_ngrams(sample_phrase, n=2))
print("Question 4 Output (Trigrams):\n", generate_ngrams(sample_phrase, n=3))




# 5. Term Frequency (TF) Counter
# The Challenge:
# Before text can be fed into a machine learning model, it must be converted into numbers.
#  Write a script to calculate the normalized term frequency of words in a document after cleaning it.
# Formula: \(\text{TF}(t) = \frac{\text{Number of times term } t \text{ appears in a document}}{\text{Total number of terms in the document}}\)
#  Steps:
#  Clean the text (lowercase, remove punctuation, remove stop words).
# Compute the total count of each unique remaining word.
# Return a Python dictionary mapping {word: tf_score} sorted by the highest score first. 





import string
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

def calculate_term_frequency(text: str) -> dict[str, float]:
    # 1. Clean & Lowercase
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = clean_text.split()
    
    # 2. Filter out stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and word.strip() != '']
    
    total_tokens = len(filtered_tokens)
    if total_tokens == 0:
        return {}
        
    # 3. Count frequencies
    word_counts = Counter(filtered_tokens)
    
    # 4. Normalize score: (word_count / total_filtered_tokens)
    tf_scores = {word: count / total_tokens for word, count in word_counts.items()}
    
    # Sort dictionary by score descending
    return dict(sorted(tf_scores.items(), key=lambda item: item[1], reverse=True))

# --- Test ---
document = "Data science is data driven. Science tracks data patterns for deep intelligence."
print("\nQuestion 5 Output:\n", calculate_term_frequency(document))
