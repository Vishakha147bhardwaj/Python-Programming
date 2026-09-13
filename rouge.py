# To use this in production, you would run: pip install rouge-score
from rouge_score import rouge_scorer

# Step 1: Initialize the scorer with desired metric variants
# We track word-level (rouge1), phrase-level (rouge2), and structural-level (rougeL) metrics
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Step 2: Define the baseline human gold standard
reference_summary = "The central bank cut interest rates by 0.5 percent to boost the struggling economy."

# Step 3: Define model outputs
# Candidate A: Captures the core message well
candidate_good = "Interest rates were cut by 0.5% by the central bank to stimulate economic growth."

# Candidate B: Missing critical context (omitted the rate details and the core reason)
candidate_short = "The central bank changed interest rates."

# Step 4: Compute scores
scores_good = scorer.score(reference_summary, candidate_good)
scores_short = scorer.score(reference_summary, candidate_short)

# Step 5: Extract and print the F1-Scores
print("--- Good Summary Scores ---")
print(f"ROUGE-1 F1: {scores_good['rouge1'].fmeasure:.4f}")
print(f"ROUGE-2 F1: {scores_good['rouge2'].fmeasure:.4f}")
print(f"ROUGE-L F1: {scores_good['rougeL'].fmeasure:.4f}\n")

print("--- Short/Incomplete Summary Scores ---")
print(f"ROUGE-1 F1: {scores_short['rouge1'].fmeasure:.4f}")
print(f"ROUGE-2 F1: {scores_short['rouge2'].fmeasure:.4f}")
print(f"ROUGE-L F1: {scores_short['rougeL'].fmeasure:.4f}")
