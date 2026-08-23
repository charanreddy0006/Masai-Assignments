"""
SupportAI - LLM Integration

This module provides the LLM layer for SupportAI.

Responsibilities:
    1. Load the Groq API key securely from environment variables.
    2. Create a Groq client.
    3. Send a user's question together with the selected FAQ.
    4. Generate a clear, FAQ-grounded response.

LLM Provider:
    Groq

Model:
    openai/gpt-oss-120b
"""

import os

from dotenv import load_dotenv
from groq import Groq


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Load variables from the .env file.
load_dotenv()


MODEL_NAME = "openai/gpt-oss-120b"


# ---------------------------------------------------------------------------
# Groq Client
# ---------------------------------------------------------------------------

def create_groq_client():
    """
    Create and return a configured Groq API client.

    The API key is loaded from the GROQ_API_KEY environment variable.

    Returns:
        Groq: Configured Groq client.

    Raises:
        RuntimeError: If GROQ_API_KEY is not configured.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. "
            "Please add your Groq API key to the .env file."
        )

    return Groq(api_key=api_key)


# ---------------------------------------------------------------------------
# Prompt Construction
# ---------------------------------------------------------------------------

def build_prompt(question, faq):
    """
    Build the user prompt using the customer's question and FAQ context.

    The FAQ information is provided to the model so that the generated
    answer remains grounded in the SupportAI knowledge base.

    Args:
        question (str):
            The customer's natural-language question.

        faq (dict):
            The selected FAQ entry.

    Returns:
        str:
            Formatted prompt for the LLM.
    """

    return f"""
FAQ CONTEXT
-----------

Category:
{faq["category"]}

FAQ Question:
{faq["question"]}

Official FAQ Answer:
{faq["answer"]}


CUSTOMER QUESTION
-----------------

{question}


TASK
----

Answer the customer's question using the FAQ information above.

Rules:
- Use only information provided in the FAQ.
- Do not invent information.
- Do not create policies, prices, dates, or procedures.
- Give a clear and friendly response.
- Keep the answer concise.
- If the FAQ does not contain enough information, clearly say that
  the available knowledge base does not contain enough information.
"""


# ---------------------------------------------------------------------------
# LLM Response Generation
# ---------------------------------------------------------------------------

def generate_answer(question, faq):
    """
    Generate a natural-language answer using the Groq LLM.

    Args:
        question (str):
            The customer's question.

        faq (dict):
            The FAQ selected by the search system.

    Returns:
        str:
            The generated SupportAI response.

    Raises:
        RuntimeError:
            If the API key is missing or the API request fails.
    """

    client = create_groq_client()

    system_prompt = """
You are SupportAI, an intelligent customer support assistant.

Your job is to answer customer questions using the provided FAQ
knowledge base.

Follow these rules strictly:

1. Answer using only the provided FAQ information.
2. Never invent information that is not present in the FAQ.
3. Do not make up policies, prices, dates, or procedures.
4. Be helpful, professional, and friendly.
5. Keep responses concise and easy to understand.
6. If the FAQ does not contain enough information, honestly state
   that the knowledge base does not provide enough information.
"""

    user_prompt = build_prompt(question, faq)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            temperature=0.2,
            max_tokens=300,
            include_reasoning=False,
        )

        answer = response.choices[0].message.content

        if not answer:
            raise RuntimeError(
                "Groq returned an empty response."
            )

        return answer.strip()

    except Exception as error:
        raise RuntimeError(
            f"Groq API request failed: {error}"
        ) from error


# ---------------------------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # A sample FAQ is used here only to test the LLM module.
    # The actual application will obtain FAQs from faq_search.py.
    test_faq = {
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
    }

    test_question = "I forgot my password. How can I reset it?"

    print("=" * 60)
    print("SupportAI - Task 2: Groq LLM Test")
    print("=" * 60)

    print("\nModel:")
    print(MODEL_NAME)

    print("\nUser:")
    print(test_question)

    try:
        answer = generate_answer(
            test_question,
            test_faq,
        )

        print("\nSupportAI:")
        print(answer)

        print("\n" + "=" * 60)
        print("LLM test completed successfully.")
        print("=" * 60)

    except RuntimeError as error:

        print("\nError:")
        print(error)