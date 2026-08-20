# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
# analyzer = SentimentIntensityAnalyzer() 
# text = "I absolutely love this product!" 
# scores = analyzer.polarity_scores(text) 
# print(scores)
from textblob import TextBlob
text = "I absolutely love this product!"

analysis = TextBlob(text)

print(analysis.sentiment)