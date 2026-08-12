import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Our raw, messy input text
raw_text = "The marketing campaigns are running smoothly! Analysts studied 1000+ keywords."

print(f"0. Raw Text: {raw_text}\n")

# --- STEP 1 & 2: Lowercasing & Punctuation Removal ---
# string.punctuation is just a list of all symbols: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
text_clean = raw_text.lower()
# str.maketrans(x,y,z) x = characters to replace, y = characters to replace with, z = characters to delete
replacement_table = str.maketrans('', '', string.punctuation)
text_clean = text_clean.translate(replacement_table)
print(f"1 & 2. Lowercase & No Punctuation: {text_clean}")

# --- STEP 3: Tokenisation ---
tokens = word_tokenize(text_clean)
print(f"3. Tokenised List: {tokens}")
# ['the', 'marketing', 'campaigns', 'are', 'running', 'smoothly', 'analysts', 'studied', '1000', 'keywords']
# --- STEP 4: Stop Words Removal ---
stop_words = set(stopwords.words('english'))
# Filter out words like 'the', 'are'
filtered_tokens = [word for word in tokens if word not in stop_words]
# ['marketing', 'campaigns', 'running', 'smoothly', 'analysts', 'studied', '1000', 'keywords']
print(f"4. Without Stop Words: {filtered_tokens}")

# --- STEP 5A: Stemming (The Axe) ---
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print(f"5A. Stemmed Output: {stemmed_words}")
# Notice 'marketing' becomes 'market', 'campaigns' becomes 'campaign', but 'studied' becomes 'studi' 

# --- STEP 5B: Lemmatisation (The Scalpel) ---
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print(f"5B. Lemmatized Output: {lemmatized_words}")
# Notice 'studied' becomes 'studied' (or 'study' if parts of speech are provided), remaining a real word!
