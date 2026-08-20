import re
from collections import Counter

def analyze_keyword_density(html_body_text, abuse_threshold=0.05):
    """
    Cleans text, calculates exact token frequencies, and flags SEO density anomalies.
    """
    # 1. Normalize and strip non-alpha characters via regex
    clean_text = html_body_text.lower()
    words = re.findall(r'\b[a-z]{2,}\b', clean_text)  # Only words with 2+ characters
    total_tokens = len(words)
    
    if total_tokens == 0:
        return {}

    # 2. Compute absolute frequencies
    token_counts = Counter(words)
    
    # 3. Calculate relative density metrics
    density_report = {}
    for word, count in token_counts.items():
        density = count / total_tokens
        is_stuffed = density > abuse_threshold
        
        density_report[word] = {
            "absolute_count": count,
            "density_percentage": round(density * 100, 2),
            "flag_abuse": is_stuffed
        }
        
    return density_report, total_tokens

# Execution Pipeline
raw_web_copy = """
Optimize your website using our premium SEO tool. Our SEO tool provides advanced 
SEO metrics. If you want the best SEO results, buy this SEO software today.
"""

report, total_words = analyze_keyword_density(raw_web_copy, abuse_threshold=0.06)

print(f"Total Processed Tokens: {total_words}")
print(f"{'Keyword':<12} | {'Density %':<10} | {'Abuse Flag':<10}")
print("-" * 40)
for kw, metrics in sorted(report.items(), key=lambda x: x[1]['density_percentage'], reverse=True)[:3]:
    print(f"{kw:<12} | {metrics['density_percentage']:<10} | {str(metrics['flag_abuse']):<10}")
