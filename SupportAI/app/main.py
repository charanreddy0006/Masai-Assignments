"""
SupportAI - Complete Helpdesk Agent

Task 4 integrates:
    - Task 1: FAQ knowledge base and keyword search
    - Task 2: Groq LLM integration
    - Task 3: TF-IDF + hybrid FAQ matching

The application:
    1. Accepts a user's natural-language question.
    2. Finds the best FAQ using the hybrid matcher.
    3. Checks the confidence score.
    4. Sends confident matches to the Groq LLM.
    5. Escalates questions that cannot be answered confidently.
    6. Runs continuously until the user enters 'quit' or 'exit'.
"""

from app.matcher import find_best_match
from app.llm import generate_answer
from data.faqs import faqs


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Minimum confidence required before using an FAQ.
CONFIDENCE_THRESHOLD = 0.40


# ---------------------------------------------------------------------------
# Display Functions
# ---------------------------------------------------------------------------

def print_banner():
    """
    Display the SupportAI application banner and available commands.
    """

    print("=" * 60)
    print("        SupportAI - Helpdesk Agent")
    print("=" * 60)
    print("Type 'help' for available commands.")
    print("Type 'quit' or 'exit' to close SupportAI.")
    print("=" * 60)


def print_help():
    """
    Display the commands supported by SupportAI.
    """

    print("\nSupportAI Commands")
    print("-" * 30)
    print("help  - Show available commands")
    print("quit  - Exit SupportAI")
    print("exit  - Exit SupportAI")
    print()


def print_escalation():
    """
    Display the response used when no FAQ can confidently
    answer the user's question.
    """

    print("\nSupportAI [confidence: 0.00]:")
    print(
        "I don't have enough information about that "
        "in my knowledge base."
    )
    print(
        "Would you like me to connect you with a "
        "human support agent?"
    )


# ---------------------------------------------------------------------------
# Question Processing
# ---------------------------------------------------------------------------

def process_question(question):
    """
    Process one customer question using the FAQ matcher and LLM.

    Args:
        question (str):
            The customer's natural-language question.
    """

    # Find the best FAQ match.
    result = find_best_match(
        faqs,
        question,
    )

    # No suitable FAQ was found.
    if result is None:
        print_escalation()
        return

    faq = result["faq"]
    confidence = result["confidence"]

    # Reject matches below the confidence threshold.
    if confidence < CONFIDENCE_THRESHOLD:
        print_escalation()
        return

    # Display the selected FAQ and confidence score.
    print(
        f"\nSupportAI "
        f"[confidence: {confidence:.2f}, faq: {faq['id']}] :"
    )

    try:
        # Generate a natural-language response using Groq.
        answer = generate_answer(
            question,
            faq,
        )

        print()
        print(answer)

    except RuntimeError as error:
        print("\nSupportAI:")
        print(
            "I'm sorry, but I'm currently unable to generate "
            "a response."
        )
        print(f"\nTechnical error: {error}")


# ---------------------------------------------------------------------------
# Main Application Loop
# ---------------------------------------------------------------------------

def run():
    """
    Start the interactive SupportAI helpdesk application.

    The application continues accepting questions until the user
    enters 'quit', 'exit', or terminates the program.
    """

    print_banner()

    while True:

        try:
            question = input("\nYou: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\n\nThank you for using SupportAI. Goodbye!")
            break

        # Handle empty input.
        if not question:
            print("Please enter a question.")
            continue

        command = question.lower()

        # Exit commands.
        if command in {"quit", "exit"}:
            print("\nThank you for using SupportAI. Goodbye!")
            break

        # Help command.
        if command == "help":
            print_help()
            continue

        # Process a normal customer question.
        process_question(question)


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run()