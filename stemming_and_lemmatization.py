import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

words_to_test = ["leaves", "crying", "better", "studies"]

# 1. Stemming setup
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in words_to_test]

# 2. Lemmatisation setup
lemmatizer = WordNetLemmatizer()
# Note: For 'better', we explicitly tell it it's an adjective ('a') to get 'good'
lemmatized = [lemmatizer.lemmatize(word) if word != "better" else lemmatizer.lemmatize(word, pos='a') for word in words_to_test]

print(f"{'Original':<12} | {'Stemming':<12} | {'Lemmatisation':<12}")
print("-" * 42)
for orig, stem, lemma in zip(words_to_test, stemmed, lemmatized):
    print(f"{orig:<12} | {stem:<12} | {lemma:<12}")
