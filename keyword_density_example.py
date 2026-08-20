import re
from collections import Counter

def agent_content_vetting(html_raw_text, max_allowed_density=0.05):
    """
    An internal function an AI Agent uses to decide if a webpage is spam 
    before wasting token costs reading it.
    """
    # Clean text using regular expressions (extract lowercase words only)
    words = re.findall(r'\b[a-z]{3,}\b', html_raw_text.lower())
    total_words = len(words)
    
    if total_words == 0:
        return "REJECTED: Empty Document", {}
        
    word_counts = Counter(words)
    is_spam = False
    flagged_words = []
    
    # Calculate density for each word
    for word, count in word_counts.items():
        density = count / total_words
        if density > max_allowed_density:
            is_spam = True
            flagged_words.append(f"{word} ({density*100:.1f}%)")
            
    if is_spam:
        decision = f"REJECTED: Malicious SEO Stuffing Detected! Flagged terms: {', '.join(flagged_words)}"
    else:
        decision = "APPROVED: High-quality natural text distribution. Safe to process."
        
    return decision, word_counts.most_common(3)

# --- Agent Scenario 1: A spammy competitor page ---
bad_page = "Buy cheap insurance today. Our cheap insurance plans offer cheap insurance rates."
decision, top_terms = agent_content_vetting(bad_page)
print(f"Agent Decision 1: {decision}")

# --- Agent Scenario 2: A natural blog post ---
good_page = "Our team specializes in health insurance plans, providing excellent coverage options for families. This insurance covers  full family of four, ensuring peace of mind and financial security. Our plans are designed to meet the needs of every family member."
decision, top_terms = agent_content_vetting(good_page, max_allowed_density=2)
print(f"Agent Decision 2: {decision}")
