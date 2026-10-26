"""Phase 4 starter: keyword search over FAQ entries with TF-IDF.

Run:  python phase-4-nlp-deep-learning/tfidf_search.py
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQS = [
    "How do I reset my password? Go to Settings, choose Security, then Reset password.",
    "Why is my device not syncing? Check your internet connection and sign out and back in.",
    "How can I update my billing details? Open Account, then Billing, and edit your card.",
    "How do I turn on two-factor authentication? Open Security settings and enable 2FA.",
    "My battery drains quickly. Lower screen brightness and close background apps.",
    "How do I cancel my subscription? Go to Account, then Subscriptions, then Cancel.",
]

vectorizer = TfidfVectorizer(stop_words="english")
doc_vectors = vectorizer.fit_transform(FAQS)  # one row per FAQ, one column per word


def search(query: str, k: int = 3) -> list[tuple[float, str]]:
    """Return the top-k FAQs by cosine similarity to the query."""
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    ranked = sorted(zip(scores, FAQS), reverse=True)
    return ranked[:k]


if __name__ == "__main__":
    for q in ["forgot my password", "stop paying every month", "phone dies fast"]:
        print(f"\nQuery: {q}")
        for score, text in search(q):
            print(f"  {score:.2f}  {text[:70]}")

    # ------------------------------------------------------------------
    # YOUR TURN:
    # 1. Which of the three queries above find the right FAQ? Which fail? Why?
    #    (Hint: TF-IDF only matches words that appear in both texts.)
    # 2. Print vectorizer.get_feature_names_out() and look at the vocabulary.
    # 3. Write 10 more queries, some using the FAQ's words and some paraphrased.
    #    Record how often the right FAQ is ranked first.
    # 4. After installing requirements-llm.txt, repeat this with embeddings:
    #      from sentence_transformers import SentenceTransformer
    #      model = SentenceTransformer("all-MiniLM-L6-v2")
    #      vectors = model.encode(FAQS, normalize_embeddings=True)
    #    Score the same queries and compare.
    # ------------------------------------------------------------------
