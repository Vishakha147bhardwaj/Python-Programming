# 🧼 Part 1: Text Preprocessing
# Question 1: Clean and Tokenise (Easy)
# Write a Python function clean_and_tokenize(text) that takes a string, 
# converts it to lowercase, removes all punctuation using re or built-in methods,
#  and returns a list of individual word tokens.

import re

def clean_and_tokenize(text: str) -> list:
    # 1. Convert the entire block of text to lowercase
    lowered_text = text.lower()
    
    # 2. Use a regular expression to match anything that is NOT a word character (\w) or whitespace (\s)
    # This strips punctuation while leaving numbers and letters intact.
    cleaned_text = re.sub(r'[^\w\s]', '', lowered_text)
    
    # 3. Split the clean string by whitespace blocks to isolate individual tokens
    tokens = cleaned_text.split()
    
    return tokens

# Verification Test Execution
test_input = "Hello, World! Welcome to NLP 101."
print("=== Output 1: Tokenization ===")
print(clean_and_tokenize(test_input))
# Expected Output: ['hello', 'world', 'welcome', 'to', 'nlp', '101']


# Question 2: Stop Words Filter & Basic Stemming (Medium)
# Write a function filter_and_stem(tokens) that removes a specific set of stop words
#  from a token list and applies basic rule-based suffix truncation to strip common trailing 
# endings like "ing", "es", and "s".
def filter_and_stem(tokens: list) -> list:
    STOP_WORDS = {'is', 'the', 'a', 'and', 'in', 'to', 'for'}
    processed_tokens = []
    
    for token in tokens:
        # 1. Skip appending if the token belongs to our hardcoded stop words dictionary set
        if token in STOP_WORDS:
            continue
            
        # 2. Implement basic rule-based stemming checks
        if token.endswith("ing"):
            stemmed = token[:-3]  # Strip out 'ing' trailing characters
        elif token.endswith("es"):
            stemmed = token[:-2]  # Strip out 'es' trailing characters
        elif token.endswith("s") and not token.endswith("is"):
            stemmed = token[:-1]  # Strip out generic single 's' plural character flag
        else:
            stemmed = token       # Leave token raw if no suffix parameters match
            
        processed_tokens.append(stemmed)
        
    return processed_tokens

# Verification Test Execution
test_tokens = ['the', 'engineers', 'are', 'testing', 'a', 'new', 'languages', 'framework']
print("\n=== Output 2: Stop Words & Stemming ===")
print(filter_and_stem(test_tokens))
# Expected Output: ['engineer', 'are', 'test', 'new', 'language', 'framework']


# 🏷️ Part 2: POS Tagging & NER
# Question 3: Noun and Verb Extraction via POS Tagging (Easy)
# Use spaCy's en_core_web_sm model to process a sentence. 
# Loop through the tokens and extract only the words whose part-of-speech 
# tag (.pos_) is classified as either a NOUN or a VERB.
import spacy

def extract_nouns_and_verbs(text: str) -> list:
    # 1. Load the core compact English framework dictionary transformer model
    nlp = spacy.load("en_core_web_sm")
    
    # 2. Pass the input text sequence down through the execution document processing pipeline
    doc = nlp(text)
    
    # 3. Use a list comprehension to filter out specific target part-of-speech flags
    filtered_tokens = [(token.text, token.pos_) for token in doc if token.pos_ in ("NOUN", "VERB")]
    
    return filtered_tokens

# Verification Test Execution
test_sentence = "The customer bought a laptop from the online store last night."
print("\n=== Output 3: POS Tag Extraction ===")
print(extract_nouns_and_verbs(test_sentence))
# Expected Output: [('customer', 'NOUN'), ('bought', 'VERB'), ('laptop', 'NOUN'), ('store', 'NOUN'), ('night', 'NOUN')]



# Question 4: Brand and Location Extraction via NER (Medium)
# Write a function 
# parse_web_copy_entities(web_text) using spaCy to scan a text block. Isolate and 
# return a dictionary containing two distinct sets: Organizations/Brands (ORG) and 
# Geographical Locations (GPE).

import spacy

def parse_web_copy_entities(web_text: str) -> dict:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(web_text)
    
    # Use standard python unique sets to clean out duplicates automatically
    brands_orgs = set()
    locations = set()
    
    # Loop over every item detected within the document's global '.ents' storage array
    for ent in doc.ents:
        if ent.label_ == "ORG":
            brands_orgs.add(ent.text)
        elif ent.label_ == "GPE": # GPE represents Geo-Political Entity (Countries, Cities, States)
            locations.add(ent.text)
            
    # Group results into a organized tracking dictionary wrapper payload
    return {
        'BRANDS_ORGS': brands_orgs,
        'LOCATIONS': locations
    }

# Verification Test Execution
test_copy = "Google announced that its new Pixel phone will be manufactured in India instead of China. Apple is planning similar updates for Cupertino."
print("\n=== Output 4: Named Entity Recognition (NER) ===")
import pprint
pprint.pprint(parse_web_copy_entities(test_copy))
# Expected Output: {'BRANDS_ORGS': {'Google', 'Apple'}, 'LOCATIONS': {'India', 'China', 'Cupertino'}}



# 📈 Part 1: Keyword Extraction (TF-IDF & YAKE)
# Question 1 (Easy): SEO Keyword Density AnalyzerStatement: 
# Write a function calculate_keyword_density(text, target_keyword) that calculates
#  the keyword density percentage of a target word in a block of text. 
# The function should convert the text to lowercase, split it into words
#  (ignoring basic punctuation), and calculate density using the formula: 
# (Keyword Count / Total Words) * 100.
# Solution:
def calculate_keyword_density(text: str, target_keyword: str) -> float:
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    if not words:
        return 0.0
    
    keyword_count = words.count(target_keyword.lower())
    return (keyword_count / len(words)) * 100

# Test
text_copy = "SEO optimization is crucial. Good SEO strategy increases traffic, because SEO matters."
print(calculate_keyword_density(text_copy, "seo"))  # Expected: 27.27...

# Question 2 (Easy): Unsupervised Keyword Extraction via YAKEStatement:
#  Write a function extract_yake_keywords(text, max_keywords=3) that uses the yake 
# library to extract the top key phrases from a blog post. Configure the extractor 
# to look for phrases up to 2 words long (max_ngram_size=2). Return only a list of 
# the string keywords, omitting their raw scores.


# Solution:
import yake
def extract_yake_keywords(text: str, max_keywords: int = 3) -> list:
    # max_ngram_size=2 means it will look for single words and 2-word phrases
    kw_extractor = yake.KeywordExtractor(lan="en", n=2, top=max_keywords)
    keywords = kw_extractor.extract_keywords(text)
    # YAKE returns a list of tuples: (keyword, score). Lower score means more important.
    return [kw for kw, score in keywords]

# Test
blog = "Machine learning is changing software development. Machine learning models require clean data."
print(extract_yake_keywords(blog))  # Expected: ['Machine learning', 'software development', 'learning models']


# Question 3 (Medium): Finding Unique Terms using Scikit-Learn TF-IDFStatement:
#  Given a corpus of documents, write a function get_top_tfidf_words(corpus, document_index, top_n=2)
#  that uses TfidfVectorizer from sklearn to find the most uniquely important words in a specific document
#  compared to the rest of the corpus. Return a list of the top N words.

# Solution:
# Setup required in terminal: pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
def get_top_tfidf_words(corpus: list, document_index: int, top_n: int = 2) -> list:
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Get feature names (words) and vector values for the target document
    feature_names = vectorizer.get_feature_names_out()
    doc_vector = tfidf_matrix[document_index].toarray()[0]
    
    # Pair words with their TF-IDF scores and sort them descending
    word_scores = list(zip(feature_names, doc_vector))
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
    
    return [word for word, score in sorted_words[:top_n] if score > 0]

# Test
documents = [
    "Our product offers advanced automated machine learning tools.",
    "Baking standard chocolate chip cookies requires butter and sugar.",
    "Automated baking systems combine machine learning with ovens."
]
print(get_top_tfidf_words(documents, 1))  # Expected: ['baking', 'butter'] or ['chocolate', 'cookies'] etc.

# 🧠 Part 2: Text Embeddings & Semantic Similarity
# Question 4 (Medium): Content Gap Cosine SimilarityStatement:
#  Write a script using the sentence-transformers library to calculate the semantic similarity 
# between a client's landing page copy and a competitor's page copy. Use the all-MiniLM-L6-v2 
# model to generate vectors, calculate their cosine similarity score using PyTorch or NumPy, 
# and return the numerical score.


# Solution:
# Setup required in terminal: pip install sentence-transformers
from sentence_transformers import SentenceTransformer, util
def compare_content_similarity(my_copy: str, competitor_copy: str) -> float:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate vector embeddings
    embedding1 = model.encode(my_copy, convert_to_tensor=True)
    embedding2 = model.encode(competitor_copy, convert_to_tensor=True)
    
    # Calculate cosine similarity
    similarity = util.cos_sim(embedding1, embedding2)
    return float(similarity[0][0])

# Test
mine = "We build custom mobile apps for iOS and Android platforms using Flutter."
comp = "Our agency develops cross-platform mobile applications for smartphones."
print(f"Similarity: {compare_content_similarity(mine, comp):.4f}") # Expected high similarity (~0.75+)


# Question 5 (Medium): Finding Missing Content GapsStatement:
#  Imagine a competitor covers 3 subtopics on their website, while you only cover 1 
# main topic. Write a function find_content_gaps(my_topics, competitor_topics, threshold=0.5)
#  that compares each competitor topic against your topics using embeddings. If a competitor 
# topic has a similarity score lower than the threshold against all of your topics, label 
# it as a "Content Gap" and return it in a list.


# Solution:
from sentence_transformers import SentenceTransformer, util
def find_content_gaps(my_topics: list, competitor_topics: list, threshold: float = 0.5) -> list:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    my_embeddings = model.encode(my_topics, convert_to_tensor=True)
    competitor_embeddings = model.encode(competitor_topics, convert_to_tensor=True)
    
    gaps = []
    
    for i, comp_emb in enumerate(competitor_embeddings):
        # Find similarity scores against all of my topics at once
        scores = util.cos_sim(comp_emb, my_embeddings)[0]
        
        # If the highest similarity score is below the threshold, it's a gap
        if max(scores) < threshold:
            gaps.append(competitor_topics[i])
            
    return gaps

# Test
my_site = ["How to set up email marketing automation campaigns"]
comp_site = [
    "Setting up active automated emails", 
    "Advanced technical conversion rate optimization", 
    "A/B testing landing page layouts"
]
print("Missing Topics:", find_content_gaps(my_site, comp_site))
# Expected Gaps: ['Advanced technical conversion rate optimization', 'A/B testing landing page layouts']
