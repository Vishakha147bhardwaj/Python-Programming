import re
from collections import Counter

def audit_seo_density(html_article_text, target_keywords):
    # 1. Clean HTML components & lower-case (matches search engine crawlers)
    clean_text = re.sub(r'<[^>]+>', ' ', html_article_text.lower())
    words = re.findall(r'\b[a-z0-9\-]+\b', clean_text)
    total_words = len(words)
    
    reconstructed_text = " ".join(words)
    report = {"metrics": {"total_word_count": total_words}, "keywords": {}}
    
    # 2. Compute exact structural matches
    for keyword in target_keywords:
        kw_clean = keyword.lower().strip()
        kw_word_count = len(kw_clean.split())
        
        # Use regex to find overlapping or multi-word exact phrase occurrences
        occurrences = len(re.findall(rf'\b{re.escape(kw_clean)}\b', reconstructed_text))
        
        # Calculate real phrasal weight contribution
        density_percentage = ((occurrences * kw_word_count) / total_words) * 100 if total_words > 0 else 0
        
        # 3. Categorize SEO Health status
        if density_percentage == 0:
            status = "Missing Content Optimization Target"
        elif 1.0 <= density_percentage <= 2.5:
            status = "Optimal Semantic Density Range"
        elif density_percentage > 4.0:
            status = "High Risk - Keyword Stuffing Penalty Flag"
        else:
            status = "Sub-optimal Context Signal"
            
        report["keywords"][keyword] = {
            "raw_count": occurrences,
            "density_pct": round(density_percentage, 2),
            "seo_status": status
        }
        
    return report

# Execution Sample
article = "<h1>Deep Learning Systems</h1><p>Deep learning drives software. Deep learning is built on deep learning arrays.</p>"
targets = ["deep learning", "software"]
print(audit_seo_density(article, targets))
