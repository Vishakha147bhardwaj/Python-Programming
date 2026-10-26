import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# ============================================================
# 1. COSINE SIMILARITY FUNCTION
# ============================================================

def calculate_cosine_similarity(vec_a, vec_b):
    """
    Calculate cosine similarity between two vectors.

    Formula:

        cosine similarity =
        (A · B) / (||A|| × ||B||)

    Result:
        1  = very similar
        0  = not similar
       -1  = opposite
    """

    # Convert vectors to NumPy arrays
    a = np.array(vec_a)
    b = np.array(vec_b)

    # Calculate dot product
    dot_product = np.dot(a, b)

    # Calculate vector magnitudes
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    # Avoid division by zero
    if norm_a == 0 or norm_b == 0:
        return 0.0

    # Cosine similarity
    return float(dot_product / (norm_a * norm_b))


# ============================================================
# 2. MAIN FUNCTION
# ============================================================

def main():

    print("=" * 60)
    print("       TEXT SIMILARITY USING COSINE SIMILARITY")
    print("=" * 60)

    # --------------------------------------------------------
    # Two sentences to compare
    # --------------------------------------------------------

    text_a = (
        "AI powered competitor monitoring "
        "for enterprise markets"
    )

    text_b = (
        "Automated tools track competitor actions "
        "and pricing changes"
    )

    print("\nText A:")
    print(text_a)

    print("\nText B:")
    print(text_b)

    # --------------------------------------------------------
    # 3. CREATE TF-IDF VECTORS
    # --------------------------------------------------------

    vectorizer = TfidfVectorizer()

    # Convert both sentences into numerical vectors
    vectors = vectorizer.fit_transform([
        text_a,
        text_b
    ])

    # Convert sparse matrices to normal NumPy arrays
    vector_a = vectors[0].toarray()[0]
    vector_b = vectors[1].toarray()[0]

    # --------------------------------------------------------
    # 4. DISPLAY THE WORDS USED
    # --------------------------------------------------------

    words = vectorizer.get_feature_names_out()

    print("\nWords/features:")
    print(words)

    # --------------------------------------------------------
    # 5. DISPLAY THE VECTORS
    # --------------------------------------------------------

    print("\nVector A:")
    print(vector_a)

    print("\nVector B:")
    print(vector_b)

    print(f"\nVector dimension: {len(vector_a)}")

    # --------------------------------------------------------
    # 6. CALCULATE COSINE SIMILARITY
    # --------------------------------------------------------

    similarity_score = calculate_cosine_similarity(
        vector_a,
        vector_b
    )

    # --------------------------------------------------------
    # 7. DISPLAY RESULT
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("                    RESULT")
    print("=" * 60)

    print(
        f"\nCosine Similarity Score: "
        f"{similarity_score:.4f}"
    )

    # --------------------------------------------------------
    # 8. INTERPRET RESULT
    # --------------------------------------------------------

    print("\nInterpretation:")

    if similarity_score >= 0.80:
        print("Very strong similarity.")

    elif similarity_score >= 0.60:
        print("Strong similarity.")

    elif similarity_score >= 0.40:
        print("Moderate similarity.")

    elif similarity_score >= 0.20:
        print("Weak similarity.")

    else:
        print("Very low similarity.")

    print("\n" + "=" * 60)


# ============================================================
# 9. RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()