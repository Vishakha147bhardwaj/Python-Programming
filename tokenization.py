import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt') # Required resource for tokenisation

text = "Dr. Smith said, 'Don't panic!' The project is due tomorrow."

# 1. Sentence Tokenisation
sentences = sent_tokenize(text)
print("Sentences:", sentences)
# Output: ["Dr. Smith said, 'Don't panic!'", 'The project is due tomorrow.']

# 2. Word Tokenisation
words = word_tokenize(text)
print("Words:", words)
# Output: ['Dr.', 'Smith', 'said', ',', "'Do", "n't", 'panic', '!', "'", 'The', 'project', 'is', 'due', 'tomorrow', '.']
text_to_lowercase = "Natural Language Processing is AWESOME."

lowercased_text = text_to_lowercase.lower()
print(lowercased_text)