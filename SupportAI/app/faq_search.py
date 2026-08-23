"""
FAQ search functionality for SupportAI.

This module provides keyword-based searching and FAQ lookup
functions for the Task 1 knowledge base.
"""


def search_by_keyword(faqs, query):
    """
    Search FAQs using words from a user's query.

    Query words are matched case-insensitively against the
    FAQ keywords, question, and category.

    Matching FAQs are ranked by the number of matching
    keyword/query terms, with the highest score first.

    Args:
        faqs (list): List of FAQ dictionaries.
        query (str): User's search query.

    Returns:
        list: Matching FAQ dictionaries ordered by relevance.
    """

    query_words = query.lower().split()

    results = []

    for faq in faqs:
        keywords = [keyword.lower() for keyword in faq["keywords"]]
        question = faq["question"].lower()
        category = faq["category"].lower()

        score = 0

        for word in query_words:
            if any(word in keyword for keyword in keywords):
                score += 1
            elif word in question:
                score += 1
            elif word in category:
                score += 1

        if score > 0:
            results.append((score, faq))

    # Highest-scoring FAQs should appear first.
    results.sort(key=lambda item: item[0], reverse=True)

    return [faq for score, faq in results]


def get_faq_by_id(faqs, faq_id):
    """
    Find an FAQ using its unique identifier.

    Args:
        faqs (list): List of FAQ dictionaries.
        faq_id (str): FAQ identifier.

    Returns:
        dict | None: Matching FAQ or None if not found.
    """

    for faq in faqs:
        if faq["id"].lower() == faq_id.lower():
            return faq

    return None


def get_faqs_by_category(faqs, category):
    """
    Return all FAQs belonging to a category.

    Category comparison is case-insensitive.

    Args:
        faqs (list): List of FAQ dictionaries.
        category (str): Category to search for.

    Returns:
        list: FAQs belonging to the requested category.
    """

    category = category.lower()

    return [
        faq
        for faq in faqs
        if faq["category"].lower() == category
    ]


def display_search_results(query, results):
    """
    Display FAQ search results in a readable format.

    Args:
        query (str): Original search query.
        results (list): Matching FAQ dictionaries.
    """

    print(f"\nQuery: {query}")

    if not results:
        print("  No matching FAQs found.")
        return

    for faq in results:
        print(f"  [{faq['category']}] {faq['question']}")
        print(f"  → {faq['answer']}")
        print()


if __name__ == "__main__":
    from faq_data import faqs

    test_queries = [
        "forgot my password",
        "refund",
        "weather today",
    ]

    for query in test_queries:
        results = search_by_keyword(faqs, query)
        display_search_results(query, results)