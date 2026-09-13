import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Step 1: Define Ground Truth Human References
# Note: You can provide multiple valid human translations because there are many ways to translate a sentence!
# This requires a list of lists of tokens.
references = [
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
    ["a", "fast", "brown", "fox", "leaps", "across", "the", "lazy", "dog"]
]

# Step 2: Define Machine Outputs (Candidates)
candidate_good = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
candidate_ok   = ["the", "fast", "brown", "fox", "jumps", "over", "a", "lazy", "dog"]
candidate_bad  = ["the", "fox", "is", "running", "quickly", "and", "jumping"]

# Step 3: Set up a smoothing function
# Necessary for short sentences to prevent the score from dropping straight to 0 if a 4-gram doesn't match
smooth = SmoothingFunction().method1

# Step 4: Calculate and print scores
score_perfect = sentence_bleu(references, candidate_good, smoothing_function=smooth)
score_ok      = sentence_bleu(references, candidate_ok, smoothing_function=smooth)
score_bad     = sentence_bleu(references, candidate_bad, smoothing_function=smooth)

print(f"Perfect Match BLEU Score: {score_perfect:.4f}")  # Expect 1.0000
print(f"Decent Match BLEU Score:  {score_ok:.4f}")       # High score due to high n-gram overlap
print(f"Poor Match BLEU Score:    {score_bad:.4f}")      # Low score
