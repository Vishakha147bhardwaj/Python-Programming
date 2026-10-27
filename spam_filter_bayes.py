import pandas as pd
import numpy as np

# Set seed for identical distributions
np.random.seed(42)
num_emails = 10000

# 1. Simulate the Prior: 20% of emails are Spam, 80% are Safe (Ham)
is_spam = np.random.choice([True, False], size=num_emails, p=[0.20, 0.80])

contains_crypto = []
for spam_status in is_spam:
    if spam_status:
        # Spam emails have a 60% chance of mentioning 'Crypto'
        contains_crypto.append(np.random.choice([True, False], p=[0.60, 0.40]))
    else:
        # Safe emails have only a 3.75% chance of mentioning 'Crypto'
        contains_crypto.append(np.random.choice([True, False], p=[0.0375, 0.9625]))

# Construct Inbox DataFrame
inbox_df = pd.DataFrame({
    'Is_Spam': is_spam,
    'Contains_Crypto': contains_crypto
})

# --- Bayesian Component Calculations ---

# Prior: P(Spam)
p_spam = inbox_df['Is_Spam'].mean()

# Likelihood: P(Crypto | Spam)
p_crypto_given_spam = inbox_df[inbox_df['Is_Spam'] == True]['Contains_Crypto'].mean()

# Evidence Base Rate: P(Crypto)
p_crypto = inbox_df['Contains_Crypto'].mean()

# Posterior: Applying Bayes' Theorem Formula
p_spam_given_crypto = (p_crypto_given_spam * p_spam) / p_crypto

print("📩 --- BAYESIAN INBOX FILTER METRICS ---")
print(f"Prior Probability P(Spam)            : {p_spam:.2%}")
print(f"Likelihood P(Crypto | Spam)           : {p_crypto_given_spam:.2%}")
print(f"Total Evidence Base Rate P(Crypto)     : {p_crypto:.2%}\n")
print(f"🚀 Updated Posterior P(Spam | Crypto) : {p_spam_given_crypto:.2%}")
