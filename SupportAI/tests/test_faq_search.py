"""
Tests for SupportAI FAQ search functionality.
"""

from app.faq_data import faqs
from app.faq_search import (
    search_by_keyword,
    get_faq_by_id,
    get_faqs_by_category,
)


def test_password_search():
    """Password-related queries should return the password FAQ."""
    results = search_by_keyword(faqs, "forgot my password")

    assert len(results) >= 1
    assert results[0]["id"] == "faq-001"


def test_refund_search():
    """Refund queries should return the billing refund FAQ."""
    results = search_by_keyword(faqs, "refund")

    assert len(results) >= 1
    assert results[0]["id"] == "faq-002"


def test_no_match_search():
    """Unrelated queries should return no FAQ results."""
    results = search_by_keyword(faqs, "weather today")

    assert results == []


def test_get_faq_by_id():
    """FAQ lookup should return the correct FAQ by ID."""
    result = get_faq_by_id(faqs, "faq-001")

    assert result is not None
    assert result["category"] == "Account"


def test_get_faq_by_invalid_id():
    """An unknown FAQ ID should return None."""
    result = get_faq_by_id(faqs, "faq-999")

    assert result is None


def test_get_faqs_by_category():
    """Category lookup should be case-insensitive."""
    results = get_faqs_by_category(faqs, "account")

    assert len(results) == 2
    assert results[0]["id"] == "faq-001"
    assert results[1]["id"] == "faq-004"


def test_category_case_insensitive():
    """Different category capitalization should produce the same results."""
    lower_results = get_faqs_by_category(faqs, "billing")
    upper_results = get_faqs_by_category(faqs, "BILLING")

    assert lower_results == upper_results