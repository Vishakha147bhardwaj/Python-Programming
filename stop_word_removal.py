import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

text = "This is a simple sample sentence showing off stop words removal."
stop_words = set(stopwords.words('english'))

words = word_tokenize(text.lower())
# words = ['this', 'is', 'a', 'simple', 'sample', 'sentence', 'showing', 'off', 'stop', 'words', 'removal', '.']
# Filter out words that are in the stop words list
filtered_words = [w for w in words if w not in stop_words]

print(filtered_words)
# Output: ['simple', 'sample', 'sentence', 'showing', 'stop', 'words', 'removal', '.']
