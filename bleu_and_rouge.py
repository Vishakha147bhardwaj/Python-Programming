import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer

# Setup NLTK tokenization and BLEU smoothing
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
smoothie = SmoothingFunction().method1

def evaluate_texts(reference, candidate):
    # 1. Calculate BLEU Score
    # NLTK expects tokenized lists: [['word1', 'word2']] for reference, ['word1', 'word2'] for candidate
    ref_tokens = [nltk.word_tokenize(reference.lower())]
    cand_tokens = nltk.word_tokenize(candidate.lower())
    
    # Weights for BLEU-4 (equal weight to 1-gram, 2-gram, 3-gram, and 4-gram)
    bleu_score = sentence_bleu(ref_tokens, cand_tokens, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smoothie)

    # 2. Calculate ROUGE Scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(reference, candidate)
    
    # Print Results
    print(f"Reference: '{reference}'")
    print(f"Candidate: '{candidate}'\n")
    print(f"BLEU-4 Score : {bleu_score:.4f}")
    print(f"ROUGE-1 (F1) : {rouge_scores['rouge1'].fmeasure:.4f} (Recall: {rouge_scores['rouge1'].recall:.4f}, Precision: {rouge_scores['rouge1'].precision:.4f})")
    print(f"ROUGE-2 (F1) : {rouge_scores['rouge2'].fmeasure:.4f}")
    print(f"ROUGE-L (F1) : {rouge_scores['rougeL'].fmeasure:.4f}")
    print("-" * 50)

# ==========================================
# TEST CASE 1: Near Perfect Match
# ==========================================
print("--- TEST CASE 1: Near Perfect Match ---")
ref_1 = "The quick brown fox jumps over the lazy dog"
cand_1 = "The quick brown fox jumped over the lazy dog" # Minor tense change
evaluate_texts(ref_1, cand_1)

# ==========================================
# TEST CASE 2: Same Meaning, Different Words (The Synonym Problem)
# ==========================================
print("--- TEST CASE 2: Synonym Match ---")
ref_2 = "The medicine is highly effective for reducing pain."
cand_2 = "This medication works incredibly well to alleviate discomfort."
evaluate_texts(ref_2, cand_2)
