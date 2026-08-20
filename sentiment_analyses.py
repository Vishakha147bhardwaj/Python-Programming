import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline

# Download VADER lexicon data if running for the first time
nltk.download('vader_lexicon', quiet=True)

# Test phrase containing mixed emotion and punctuation
sample_text = "I absolutely HATE waiting in line, but the customer support team was amazing! 😊"

print("--- 1. VADER Results ---")
vader_analyzer = SentimentIntensityAnalyzer()
vader_scores = vader_analyzer.polarity_scores(sample_text)
print(f"VADER Raw Scores: {vader_scores}")
# Compound score ranges from -1 (Neg) to +1 (Pos)
print(f"Overall VADER Sentiment: {'Positive' if vader_scores['compound'] > 0 else 'Negative'}\n")

print("--- 2. TextBlob Results ---")
blob = TextBlob(sample_text)
print(f"Polarity (Emotion): {blob.sentiment.polarity:.2f} (-1 to 1)")
print(f"Subjectivity (Opinion): {blob.sentiment.subjectivity:.2f} (0 to 1)\n")

print("--- 3. Hugging Face Results ---")
# This downloads a highly accurate, pre-trained AI model out-of-the-box
hf_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
hf_result = hf_classifier(sample_text)[0]
print(f"AI Label: {hf_result['label']} (Confidence: {hf_result['score']*100:.1f}%)")
