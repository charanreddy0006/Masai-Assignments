"""
SupportAI FAQ Knowledge Base

Shared FAQ data used by all SupportAI tasks.
"""

faqs = [
    {
        "id": "faq-001",
        "category": "Account",
        "question": "How do I reset my password?",
        "answer": (
            "Click 'Forgot Password' on the login page. "
            "Enter your registered email address and check your inbox "
            "for a reset link valid for 24 hours."
        ),
        "keywords": [
            "password",
            "reset",
            "forgot",
            "login",
        ],
    },
    {
        "id": "faq-002",
        "category": "Billing",
        "question": "What is your refund policy?",
        "answer": (
            "We offer full refunds within 30 days of purchase for "
            "unused subscriptions. Partial refunds are available "
            "for annual plans cancelled after 30 days."
        ),
        "keywords": [
            "refund",
            "money back",
            "cancel",
            "billing",
        ],
    },
    {
        "id": "faq-003",
        "category": "Shipping",
        "question": "How long does shipping take?",
        "answer": (
            "Standard shipping takes 5–7 business days. "
            "Express shipping (2–3 business days) is available "
            "at checkout for an additional fee."
        ),
        "keywords": [
            "shipping",
            "delivery",
            "tracking",
            "express",
        ],
    },
    {
        "id": "faq-004",
        "category": "Account",
        "question": "How do I update my email address?",
        "answer": (
            "Go to Settings → Account → Email. "
            "Enter your new email and confirm via the verification "
            "link sent to the new address."
        ),
        "keywords": [
            "email",
            "update",
            "change",
            "account",
        ],
    },
    {
        "id": "faq-005",
        "category": "Technical",
        "question": "The app keeps crashing. What should I do?",
        "answer": (
            "First, update to the latest version from the App Store "
            "or Google Play. If the issue persists, clear the app "
            "cache in Settings → Storage, then restart your device."
        ),
        "keywords": [
            "crash",
            "bug",
            "error",
            "technical",
            "app",
        ],
    },
]