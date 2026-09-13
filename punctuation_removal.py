import string

text = "Hello, world! This is a test... right?"

# string.punctuation contains: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
clean_text = text.translate(str.maketrans('', '', string.punctuation))

print(clean_text)
# Output: "Hello world This is a test right"
