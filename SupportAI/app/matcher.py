"""
SupportAI - Intelligent FAQ Matcher

Task 3:
    Hybrid FAQ matching using:
        1. Keyword matching
        2. TF-IDF similarity
        3. Hybrid confidence score

This module is reused by Task 4.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data.faqs import faqs
# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

KEYWORD_WEIGHT = 0.60
TFIDF_WEIGHT = 0.40

# Minimum score required for a confident FAQ match.
CONFIDENCE_THRESHOLD = 0.40


# ---------------------------------------------------------------------------
# Text Utilities
# ---------------------------------------------------------------------------

def normalize_text(text):
    """
    Convert text to lowercase and normalize whitespace.

    Args:
        text (str): Input text.

    Returns:
        str: Normalized text.
    """

    return " ".join(str(text).lower().split())


def calculate_keyword_score(query, faq):
    """
    Calculate the keyword matching score for an FAQ.

    Query words are compared against the FAQ's keywords,
    question, and category.

    Args:
        query (str): User's question.
        faq (dict): FAQ entry.

    Returns:
        float: Keyword matching score between 0 and 1.
    """

    query_words = set(
        normalize_text(query).split()
    )

    if not query_words:
        return 0.0

    keywords = {
        normalize_text(keyword)
        for keyword in faq.get("keywords", [])
    }

    question_words = set(
        normalize_text(faq.get("question", "")).split()
    )

    category_words = set(
        normalize_text(faq.get("category", "")).split()
    )

    searchable_words = (
        keywords
        | question_words
        | category_words
    )

    matches = query_words.intersection(searchable_words)

    return len(matches) / len(query_words)


# ---------------------------------------------------------------------------
# TF-IDF Matching
# ---------------------------------------------------------------------------

def build_faq_text(faq):
    """
    Combine the searchable FAQ fields into one text document.

    Args:
        faq (dict): FAQ entry.

    Returns:
        str: Combined FAQ text.
    """

    return " ".join(
        [
            str(faq.get("category", "")),
            str(faq.get("question", "")),
            str(faq.get("answer", "")),
            " ".join(faq.get("keywords", [])),
        ]
    )


def calculate_tfidf_scores(faqs, query):
    """
    Calculate TF-IDF cosine similarity between the query and FAQs.

    Args:
        faqs (list): List of FAQ dictionaries.
        query (str): User's question.

    Returns:
        list: TF-IDF similarity score for each FAQ.
    """

    documents = [
        build_faq_text(faq)
        for faq in faqs
    ]

    vectorizer = TfidfVectorizer(
        lowercase=True
    )

    matrix = vectorizer.fit_transform(
        documents + [query]
    )

    faq_vectors = matrix[:-1]
    query_vector = matrix[-1]

    scores = cosine_similarity(
        query_vector,
        faq_vectors
    )[0]

    return scores.tolist()


# ---------------------------------------------------------------------------
# Hybrid Matching
# ---------------------------------------------------------------------------

def find_matches(faqs, query):
    """
    Find and rank FAQs using the hybrid matching approach.

    The final score combines keyword matching and TF-IDF similarity.

    Formula:

        hybrid_score =
            0.60 * keyword_score +
            0.40 * tfidf_score

    Args:
        faqs (list):
            List of FAQ dictionaries.

        query (str):
            User's natural-language question.

    Returns:
        list:
            Ranked FAQ matches containing FAQ information,
            keyword score, TF-IDF score, and hybrid score.
    """

    if not faqs:
        return []

    tfidf_scores = calculate_tfidf_scores(
        faqs,
        query
    )

    matches = []

    for index, faq in enumerate(faqs):

        keyword_score = calculate_keyword_score(
            query,
            faq
        )

        tfidf_score = tfidf_scores[index]

        hybrid_score = (
            KEYWORD_WEIGHT * keyword_score
            + TFIDF_WEIGHT * tfidf_score
        )

        matches.append(
            {
                "faq": faq,
                "keyword_score": keyword_score,
                "tfidf_score": tfidf_score,
                "hybrid_score": hybrid_score,
            }
        )

    # Highest hybrid score first.
    matches.sort(
        key=lambda item: item["hybrid_score"],
        reverse=True
    )

    return matches


# ---------------------------------------------------------------------------
# Best Match
# ---------------------------------------------------------------------------

def find_best_match(faqs, query):
    """
    Find the highest-confidence FAQ for a user question.

    A match is returned only when its hybrid score reaches
    the configured confidence threshold.

    Args:
        faqs (list):
            List of FAQ dictionaries.

        query (str):
            User's natural-language question.

    Returns:
        dict or None:
            Dictionary containing the selected FAQ and confidence,
            or None when no confident match exists.
    """

    matches = find_matches(
        faqs,
        query
    )

    if not matches:
        return None

    best_match = matches[0]

    confidence = best_match["hybrid_score"]

    if confidence < CONFIDENCE_THRESHOLD:
        return None

    return {
        "faq": best_match["faq"],
        "confidence": confidence,
        "keyword_score": best_match["keyword_score"],
        "tfidf_score": best_match["tfidf_score"],
    }


# ---------------------------------------------------------------------------
# Task 3 Demonstration
# ---------------------------------------------------------------------------

def run_task3_demo(faqs):
    """
    Run the Task 3 demonstration queries.

    Args:
        faqs (list): FAQ knowledge base.
    """

    test_queries = [
        "I forgot my password",
        "How can I get my money back?",
        "How long will my delivery take?",
        "I want to change my email",
        "The application keeps crashing",
        "What is the weather today?",
    ]

    print("=" * 60)
    print("SupportAI - Task 3: Intelligent FAQ Matching")
    print("=" * 60)

    for query in test_queries:

        print(f"\nQuery: {query}")
        print("-" * 60)

        matches = find_matches(
            faqs,
            query
        )

        # Display the top three matches.
        for match in matches[:3]:

            faq = match["faq"]

            print(
                f"FAQ ID: {faq['id']}"
            )

            print(
                f"Category: {faq['category']}"
            )

            print(
                f"Question: {faq['question']}"
            )

            print(
                f"Keyword Score: "
                f"{match['keyword_score']:.4f}"
            )

            print(
                f"TF-IDF Score: "
                f"{match['tfidf_score']:.4f}"
            )

            print(
                f"Hybrid Score: "
                f"{match['hybrid_score']:.4f}"
            )

            print()

        best_match = find_best_match(
            faqs,
            query
        )

        if best_match:

            print(
                f"Best Match: "
                f"{best_match['faq']['id']}"
            )

            print(
                f"Confidence: "
                f"{best_match['confidence']:.4f}"
            )

        else:

            print(
                "Best Match: "
                "No confident FAQ match"
            )


# ---------------------------------------------------------------------------
# Standalone Execution
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # Import the shared FAQ knowledge base.
    from data.faqs import faqs
    run_task3_demo(faqs)

    print("\n" + "=" * 60)
    print("Task 3 matching test completed.")
    print("=" * 60)