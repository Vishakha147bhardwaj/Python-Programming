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
from openai import OpenAI
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

# 📊 Sentiment Analysis & Text Classification
# 1. Rule-Based Sentiment: Processing Feedback with VADER 🟢 (Easy)
# Problem Statement:
# When building lightweight monitoring systems, rule-based lexicon matchers
#  are preferred for speed. Write a Python function called analyze_vader_sentiment(text)
#  that uses the vaderSentiment package. It should analyze a string and return the string 
# keyword "Positive", "Negative", or "Neutral" based on the following standard compound score thresholds:
# Positive: compound score >= 0.05
# Negative: compound score <= -0.05
# Neutral: Everything in between.

# Solution:
# First ensure you have it installed: pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    # Fetch the intensity score dictionary
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']
    
    # Classify based on standard VADER thresholds
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Testing the implementation
print(analyze_vader_sentiment("This new LLM updates are absolutely incredible!")) 
# Output: Positive
print(analyze_vader_sentiment("The latency is terrible and it keeps crashing."))   
# Output: Negative

# 2. Extracting Subjectivity with TextBlob 🟢 (Easy)
# Problem Statement:
# To filter objective user search queries from subjective reviews, you need to extract
#  meta-metrics. Write a function called get_text_subjectivity(text) using the TextBlob library.
#  The function should analyze a text block and return its raw subjectivity float score 
# (which spans from 0.0 for pure fact to 1.0 for pure opinion).

# Solution:
# First ensure you have it installed: pip install textblob
from textblob import TextBlob

def get_text_subjectivity(text):
    blob = TextBlob(text)
    # TextBlob sentiment returns a named tuple: (polarity, subjectivity)
    return blob.sentiment.subjectivity

# Testing the implementation
fact_text = "The Python language was created by Guido van Rossum."
opinion_text = "Python is the most beautiful and perfect language ever."

print(f"Fact Subjectivity: {get_text_subjectivity(fact_text)}")
# Output: Fact Subjectivity: 0.0 (Objective fact)
print(f"Opinion Subjectivity: {get_text_subjectivity(opinion_text)}")
# Output: Opinion Subjectivity: 0.75 (Highly subjective opinion)

# 3. Pipeline Deployment: Hugging Face Transformers 🟡 (Medium)
# Problem Statement:
# Rule-based tools struggle with nuance, sarcasm, or context. Use the Hugging Face transformers 
# library to initialize a standard deep learning pipeline for 'sentiment-analysis'. Write a function
#  deep_analyze_sentiment(text_list) that takes a list of text strings, passes them through a pre-trained
#  Transformer model pipeline, and extracts only the text label ('POSITIVE' or 'NEGATIVE') for each input 
# into a flat list.

# Solution:
# First ensure you have them installed: pip install transformers torch
from transformers import pipeline

# Initialize the pipeline once globally to avoid reloading models constantly
sentiment_pipeline = pipeline('sentiment-analysis')

def deep_analyze_sentiment(text_list):
    results = sentiment_pipeline(text_list)
    # Extract only the 'LABEL' value from the generated dictionaries
    return [item['label'] for item in results]

# Testing the implementation
sentences = [
    "I'm not saying it's bad, but I definitely wouldn't buy it again.",
    "This solution works flawlessly!"
]
print(deep_analyze_sentiment(sentences))
# Output: ['NEGATIVE', 'POSITIVE']

# 4. Rule-Based Routing: Classifying Search Intent 🟡 (Medium)
# Problem Statement:
# Before hitting an expensive LLM, routing search engine phrases can save massive costs. 
# Create a function classify_search_intent(query) that flags basic user search intents 
# using simple keyword checking. 
# Classify into three buckets:transactional: 
# If the query contains words like "buy", "price", "discount", or "order".
# navigational: If the query contains platform names like "login", "signin", "download", or "homepage".
# informational: If it doesn't match the above and contains question words like "how", "what", "why", or "guide".
# Return "unknown" if no matches occur.

# Solution:
def classify_search_intent(query):
    # Normalize input for matching uniformity
    query_lower = query.lower()
    
    # Keyword list definitions
    transactional_keywords = ["buy", "price", "discount", "order", "cost"]
    navigational_keywords = ["login", "signin", "download", "homepage"]
    informational_keywords = ["how", "what", "why", "guide", "tutorial"]
    
    # Conditional checks
    if any(word in query_lower for word in transactional_keywords):
        return "transactional"
    elif any(word in query_lower for word in navigational_keywords):
        return "navigational"
    elif any(word in query_lower for word in informational_keywords):
        return "informational"
    else:
        return "unknown"

# Testing the implementation
print(classify_search_intent("Where can I buy a cheap mechanical keyboard?")) # Output: transactional
print(classify_search_intent("JupyterLab login dashboard"))                   # Output: navigational
print(classify_search_intent("How to build a custom transformer network"))    # Output: informational

# 5. Intent Routing to Agent Pipelines 🟡 (Medium)
# Problem Statement:
# Combine classification and modular architecture. Create a class QueryRouter. It should have an instance method route_query(user_query).
# First, use the structural heuristic logic from Question 4 to determine the user's intent.
# Next, return a string that instructs an downstream engine where to deliver the data.
# If "transactional", return "Sent to Sales Pipeline".
# If "informational", return "Sent to Knowledge Base RAG Pipeline".
# For everything else, return "Sent to General Help Desk Queue".

# Solution:

class QueryRouter:
    def __init__(self):
        pass
        
    def _get_intent(self, text):
        # Internal helper method implementing search routing heuristics
        text = text.lower()
        if any(w in text for w in ["buy", "price", "purchase"]):
            return "transactional"
        elif any(w in text for w in ["how", "what", "explain", "tutorial"]):
            return "informational"
        return "other"
        
    def route_query(self, user_query):
        intent = self._get_intent(user_query)
        
        # Determine target system execution based on classification
        if intent == "transactional":
            return "Sent to Sales Pipeline"
        elif intent == "informational":
            return "Sent to Knowledge Base RAG Pipeline"
        else:
            return "Sent to General Help Desk Queue"

# Testing the implementation
router = QueryRouter()
print(router.route_query("What is the difference between VADER and HuggingFace?"))
# Output: Sent to Knowledge Base RAG Pipeline
print(router.route_query("Purchase premium API access keys"))
# Output: Sent to Sales Pipeline


# 🧠 Topic: Introduction to Large Language Models (LLMs)
# Question 1: Text Tokenization and Context Window Slicing
# Problem Statement:Write a Python function slice_to_context_window(text, max_tokens, model_name="gpt-4o")
#  using the tiktoken library. The function must tokenize the raw input string, determine if the token count
#  exceeds max_tokens, and if so, slice the token array to fit exactly within the limit before decoding it 
# back into a clean string.

# Solution:
import tiktoken

def slice_to_context_window(text, max_tokens, model_name="gpt-4o"):
    # Dynamically fetch the encoding tokenizer target for the model
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(text)
    
    # Check window size constraints and slice text array if necessary
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        
    return encoding.decode(tokens)

# Question 2: OpenAI API Hyperparameter Temperature and Top-P Controls
# Problem Statement:
# Write a Python function call_llm_with_sampling(prompt, temperature, top_p) using 
# the modern openai Python SDK (v1.0.0+). Configure the client to pass the input prompt
#  into a gpt-4o-mini chat completion model, overriding default generation variables dynamically
#  using the provided parameters. Return the plaintext content of the response.

from openai import OpenAI

def call_llm_with_sampling(prompt, temperature, top_p):
    # Initializes client using environment variable OPENAI_API_KEY implicitly
    client = OpenAI()
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,  # Controls randomness/creativity spectrum
        top_p=top_p              # Controls nucleus sampling boundaries
    )
    return response.choices[0].message.content


# Question 3: Dynamic Chain-of-Thought Few-Shot Prompt Builder
# Problem Statement:
# Write a function build_reasoning_prompt(question, examples) where examples 
# is a list of dictionaries containing prior math puzzles (keys: "q", "thought", "a").
#  Use structural f-strings to dynamically assemble a Few-Shot Chain-of-Thought (CoT)
#  prompt container ensuring it ends with a structured instruction forcing the model 
# to write out its intermediate reasoning steps.

# Solution:
def build_reasoning_prompt(question, examples):
    prompt_segments = ["System: Solve the problem using step-by-step logic.\n"]
    
    # Iteratively append explicit Few-Shot exemplars detailing thought pathways
    for ex in examples:
        prompt_segments.append(
            f"Question: {ex['q']}\nReasoning: {ex['thought']}\nAnswer: {ex['a']}"
        )
    
    # Inject final execution target containing the new question block
    prompt_segments.append(
        f"Question: {question}\nReasoning: Let's think step by step."
    )
    
    return "\n\n---\n\n".join(prompt_segments)

# Question 4: Abstractive Summarisation vs. Topic Modelling with LDA
# Problem Statement:
# Given a tokenized list of text documents, write a Python function 
# extract_lda_topics(tokenized_docs, num_topics=3) using gensim. 
# Build a Dictionary corpus object, construct a Bag-of-Words (BoW) 
# frequency matrix mapping, and train a LdaModel. Return a structured 
# list containing the primary keyword distributions identifying the requested 
# number of latent topics.

# Solution:
from gensim.corpora import Dictionary
from gensim.models import LdaModel

def extract_lda_topics(tokenized_docs, num_topics=3):
    # Mapping corpus tokens to an indexed token id vocabulary matrix
    dictionary = Dictionary(tokenized_docs)
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
    
    # Train the Latent Dirichlet Allocation statistical structure
    lda = LdaModel(
        corpus=corpus, 
        id2word=dictionary, 
        num_topics=num_topics, 
        passes=10, 
        random_state=42
    )
    
    # Extract string representations of hidden semantic keyword topics
    return lda.print_topics(num_topics=num_topics, num_words=5)


# Question 5: Programmatic NLP Evaluation Metrics: BLEU and ROUGE
# Problem Statement:
# Write a Python function evaluate_output_quality(candidate, reference) using 
# evaluate or standard nltk and rouge_score libraries. The function must calculate 
# and return a dictionary containing two specific evaluation metrics: the BLEU score 
# (sentence level) and the ROUGE-L F1-score comparing the model output against the reference string.

# Solution:
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

def evaluate_output_quality(candidate, reference):
    # Tokenize words for standard NLTK sentence-level calculations
    candidate_tokens = candidate.split()
    reference_tokens = [reference.split()]
    
    # Compute BLEU with smoothing to handle short strings gracefully
    smoother = SmoothingFunction().method1
    bleu = sentence_bleu(reference_tokens, candidate_tokens, smoothing_function=smoother)
    
    # Set up and evaluate ROUGE metrics (specifically extraction-based longest common subsequence)
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    rouge_l_f1 = scores['rougeL'].fmeasure
    
    return {
        "bleu_score": bleu,
        "rouge_l_f1_score": rouge_l_f1
    }
