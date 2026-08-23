# SupportAI — Intelligent FAQ Helpdesk Agent

SupportAI is a Python-based intelligent FAQ helpdesk agent that answers customer questions using a structured FAQ knowledge base, keyword matching, TF-IDF similarity, hybrid confidence scoring, and an LLM-powered response generation layer.

The project is designed as a four-stage pipeline where each task builds on the previous one:

```text
Customer Question
       │
       ▼
┌──────────────────────────┐
│ FAQ Knowledge Base       │
│ Task 1                   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Intelligent FAQ Matcher  │
│ Keyword + TF-IDF         │
│ Task 3                   │
└────────────┬─────────────┘
             │
             ▼
       Confidence Check
             │
       ┌─────┴─────┐
       │           │
   Confident    Low Confidence
       │           │
       ▼           ▼
┌──────────────┐  Human
│ Groq LLM     │  Escalation
│ Task 2       │
└──────┬───────┘
       │
       ▼
 Natural Language
 Customer Response
```

---

## Project Overview

Modern customer support systems receive many repetitive questions related to:

- Password resets
- Refund policies
- Shipping and delivery
- Account settings
- Technical problems

SupportAI provides an automated first level of support by searching a predefined FAQ knowledge base and generating a natural-language answer when a sufficiently confident FAQ match is found.

If the system cannot confidently identify a relevant FAQ, it does not invent an answer. Instead, it informs the customer that the available knowledge base does not contain enough information and suggests escalation to a human support agent.

---

## Objectives

The project demonstrates:

1. Building a structured FAQ knowledge base.
2. Implementing keyword-based search.
3. Integrating an external LLM API.
4. Implementing TF-IDF similarity matching.
5. Combining keyword and TF-IDF scores.
6. Calculating FAQ matching confidence.
7. Applying confidence thresholds.
8. Generating FAQ-grounded responses using an LLM.
9. Handling unknown or unsupported questions.
10. Combining multiple independent modules into one application.

---

## Project Tasks

The project is divided into four tasks.

| Task | Description | Status |
|------|-------------|--------|
| Task 1 | FAQ Knowledge Base + Keyword Search | Completed |
| Task 2 | Groq LLM Integration | Completed |
| Task 3 | TF-IDF + Hybrid FAQ Matching | Completed |
| Task 4 | Complete Conversational Helpdesk Agent | Completed |

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.10+ |
| LLM Provider | Groq |
| LLM Model | `openai/gpt-oss-120b` |
| FAQ Storage | Python data structures |
| Data Processing | Python |
| Keyword Matching | Python |
| TF-IDF | scikit-learn |
| Similarity | Cosine Similarity |
| Environment Variables | python-dotenv |
| API Communication | Groq Python SDK |

---

## Project Structure

```text
SupportAI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │   ├── Complete conversational application
│   │   ├── User interaction loop
│   │   ├── Confidence checking
│   │   ├── LLM integration
│   │   └── Human escalation
│   │
│   ├── faq_search.py
│   │   ├── Keyword-based FAQ search
│   │   ├── FAQ lookup by ID
│   │   └── FAQ filtering by category
│   │
│   ├── matcher.py
│   │   ├── Keyword scoring
│   │   ├── TF-IDF vectorization
│   │   ├── Cosine similarity
│   │   ├── Hybrid scoring
│   │   └── Best FAQ selection
│   │
│   └── llm.py
│       ├── Groq client configuration
│       ├── Prompt construction
│       └── FAQ-grounded response generation
│
├── data/
│   ├── __init__.py
│   └── faqs.py
│       └── Structured FAQ knowledge base
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Task 1 — FAQ Knowledge Base

The first stage establishes the foundation of SupportAI.

Each FAQ contains:

```python
{
    "id": "faq-001",
    "category": "Account",
    "question": "How do I reset my password?",
    "answer": "...",
    "keywords": [
        "password",
        "reset",
        "forgot",
        "login"
    ]
}
```

### FAQ Fields

| Field | Description |
|-------|-------------|
| `id` | Unique FAQ identifier |
| `category` | FAQ topic |
| `question` | Official FAQ question |
| `answer` | Official answer |
| `keywords` | Search terms related to the FAQ |

Current knowledge base:

```text
faq-001 → Password Reset
faq-002 → Refund Policy
faq-003 → Shipping
faq-004 → Email Update
faq-005 → Application Crash
```

---

## Keyword Search

Task 1 implements three main functions.

### `search_by_keyword()`

Searches FAQ entries using words from:

- `keywords`
- `question`
- `category`

The comparison is case-insensitive.

Example:

```text
Query:
forgot my password

Result:
faq-001
How do I reset my password?
```

### `get_faq_by_id()`

Retrieves a specific FAQ using its unique ID.

```python
get_faq_by_id(faqs, "faq-001")
```

### `get_faqs_by_category()`

Returns all FAQs belonging to a specified category.

```python
get_faqs_by_category(faqs, "Account")
```

---

## Task 2 — Groq LLM Integration

Task 2 introduces the LLM layer.

SupportAI uses the Groq API to generate conversational responses from the selected FAQ.

Current model:

```text
openai/gpt-oss-120b
```

The LLM is not responsible for searching the entire knowledge base.

Instead:

```text
User Question
      │
      ▼
FAQ Matcher
      │
      ▼
Selected FAQ
      │
      ▼
Groq LLM
      │
      ▼
Natural Language Answer
```

This keeps the generated response grounded in the application's FAQ data.

---

## API Key Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The key must not be hard-coded inside Python source files.

The `.env` file should be included in `.gitignore`.

Example:

```gitignore
.env
__pycache__/
*.pyc
```

---

## FAQ-Grounded LLM Responses

The LLM receives:

```text
FAQ Category
FAQ Question
Official FAQ Answer
Customer Question
```

The prompt instructs the model to:

- Use only the provided FAQ.
- Avoid inventing information.
- Avoid creating unsupported policies.
- Provide concise answers.
- Remain friendly and professional.
- Admit when the FAQ does not contain enough information.

The LLM therefore acts as a response-generation layer rather than the source of truth.

---

## Task 3 — Intelligent FAQ Matching

Task 3 improves basic keyword search by introducing TF-IDF similarity.

The matcher combines:

```text
Keyword Score
      +
TF-IDF Score
      │
      ▼
Hybrid Score
```

---

## Keyword Matching

The keyword component compares words in the user's query with the FAQ's relevant terms.

Example:

```text
User:
I forgot my password

FAQ:
How do I reset my password?

Matching concepts:
forgot
password
```

A higher number of matching terms produces a higher keyword score.

---

## TF-IDF Matching

TF-IDF stands for:

```text
Term Frequency — Inverse Document Frequency
```

It converts text into numerical vectors so textual similarity can be calculated.

SupportAI compares:

```text
Customer Question
        ↓
FAQ Question + FAQ Answer + Keywords
```

The similarity between vectors is calculated using cosine similarity.

---

## Hybrid Matching

The final score combines keyword matching and TF-IDF similarity.

The current matcher uses:

```text
Hybrid Score =
0.60 × Keyword Score
+
0.40 × TF-IDF Score
```

Keyword matching therefore has greater influence while TF-IDF similarity provides additional text-based matching.

---

## Confidence Threshold

Task 4 uses:

```python
CONFIDENCE_THRESHOLD = 0.40
```

### Confident Match

```text
Confidence >= 0.40
```

The selected FAQ is passed to the Groq LLM.

### Low-Confidence Match

```text
Confidence < 0.40
```

The system does not generate an unsupported FAQ-based answer.

Instead it displays:

```text
I don't have enough information about that
in my knowledge base.

Would you like me to connect you with a
human support agent?
```

---

## Task 4 — Complete Helpdesk Agent

Task 4 combines all previous tasks into one interactive application.

Main application:

```text
app/main.py
```

The application continuously accepts customer questions.

Processing flow:

```text
1. Receive question
2. Search FAQ knowledge base
3. Calculate keyword score
4. Calculate TF-IDF score
5. Calculate hybrid score
6. Select best FAQ
7. Check confidence
8. Generate LLM response
9. Display response
```

---

## Complete Processing Pipeline

```text
                    User Question
                          │
                          ▼
                 ┌─────────────────┐
                 │ Input Validation│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ FAQ Matcher     │
                 └────────┬────────┘
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Keyword Matching       TF-IDF Matching
                │                   │
                └─────────┬─────────┘
                          │
                          ▼
                   Hybrid Score
                          │
                          ▼
                   Best FAQ Match
                          │
                          ▼
                 Confidence Check
                    /           \
                   /             \
          >= 0.40                 < 0.40
             │                       │
             ▼                       ▼
       Selected FAQ             Escalation
             │
             ▼
          Groq LLM
             │
             ▼
     Natural Language Answer
             │
             ▼
            User
```

---

## Running the Application

Open PowerShell in the project directory:

```powershell
cd "C:\Users\chara\OneDrive\One drive\MASAI ASSIGNMENTS\SupportAI"
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

### Configure Environment

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run SupportAI

Run the application from the project root:

```powershell
python -m app.main
```

Using module execution is recommended because the project uses package-based imports.

---

## Example Session

```text
============================================================
        SupportAI - Helpdesk Agent
============================================================
Type 'help' for available commands.
Type 'quit' or 'exit' to close SupportAI.
============================================================

You: I forgot my password

SupportAI [confidence: 0.53, faq: faq-001]:

Sure! To reset your password, just click "Forgot Password"
on the login page, enter the email address you use for the
account, and then check your inbox for a reset link.

You: How long will my delivery take?

SupportAI [confidence: 0.47, faq: faq-003]:

Standard shipping usually arrives in 5–7 business days.
If you need it faster, you can choose express shipping
at checkout.

You: I want to change my email

SupportAI [confidence: 0.55, faq: faq-004]:

Sure! To change your email address, open Settings,
go to Account → Email, enter your new email address,
and follow the verification link.

You: What is the weather today?

SupportAI [confidence: 0.00]:

I don't have enough information about that
in my knowledge base.

Would you like me to connect you with a
human support agent?

You: quit

Thank you for using SupportAI. Goodbye!
```

---

## Supported Commands

| Command | Description |
|---------|-------------|
| `help` | Displays available commands |
| `quit` | Exits the application |
| `exit` | Exits the application |

---

## Test Questions

### Password

```text
I forgot my password
```

Expected FAQ:

```text
faq-001
```

### Refund

```text
What is your refund policy?
```

Expected FAQ:

```text
faq-002
```

### Shipping

```text
How long will my delivery take?
```

Expected FAQ:

```text
faq-003
```

### Email

```text
I want to change my email
```

Expected FAQ:

```text
faq-004
```

### Technical Issue

```text
The application keeps crashing
```

Expected FAQ:

```text
faq-005
```

### Unknown Question

```text
What is the weather today?
```

Expected behavior:

```text
No confident FAQ match
        ↓
Human escalation message
```

---

## Module Responsibilities

### `data/faqs.py`

Stores the FAQ knowledge base and acts as the source of truth for supported customer questions.

### `app/faq_search.py`

Provides:

- Keyword search
- FAQ ID lookup
- Category filtering
- Task 1 demonstration

### `app/matcher.py`

Provides:

- Keyword scoring
- TF-IDF vectorization
- Cosine similarity
- Hybrid scoring
- Best FAQ selection
- Confidence calculation

### `app/llm.py`

Provides:

- Environment variable loading
- Groq client creation
- Prompt construction
- FAQ-grounded response generation
- API error handling

### `app/main.py`

Provides:

- Application startup
- User input
- Command handling
- FAQ matching
- Confidence checking
- LLM response generation
- Escalation handling
- Interactive conversation loop

---

## Error Handling

The application handles common failures.

### Missing API Key

If `GROQ_API_KEY` is missing, the application reports that the API key is not configured.

### LLM API Failure

If a Groq API request fails, SupportAI displays an error instead of silently terminating.

### Empty User Input

Empty questions are rejected:

```text
Please enter a question.
```

### Unknown Questions

Questions outside the FAQ knowledge base are not automatically answered.

The system uses the escalation flow instead.

### Keyboard Interrupt

Pressing:

```text
Ctrl + C
```

allows the application to exit gracefully.

---

## Security Considerations

Never hard-code the Groq API key:

```python
GROQ_API_KEY = "actual-secret-key"
```

Use:

```env
GROQ_API_KEY=your_secret_key
```

and load it through environment variables.

Make sure `.env` is ignored by Git.

Before committing, verify:

```powershell
git status
```

The actual secret key must never be pushed to GitHub.

---

## Requirements

The main dependencies are:

```text
groq
python-dotenv
scikit-learn
```

They are stored in:

```text
requirements.txt
```

Install them with:

```powershell
pip install -r requirements.txt
```

---

## Individual Module Testing

### Test FAQ Search

```powershell
python -m app.faq_search
```

### Test Intelligent Matcher

```powershell
python -m app.matcher
```

### Test Groq LLM

```powershell
python -m app.llm
```

### Run Complete Application

```powershell
python -m app.main
```

---

## Current System Architecture

```text
                    ┌───────────────────┐
                    │      User         │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     main.py       │
                    │ Application Layer │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    matcher.py     │
                    │ Keyword + TF-IDF  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    data/faqs.py   │
                    │ Knowledge Base    │
                    └─────────┬─────────┘
                              │
                              ▼
                       Confidence Check
                         /           \
                        /             \
                       ▼               ▼
               ┌──────────────┐   ┌──────────────┐
               │   llm.py     │   │ Escalation   │
               │  Groq LLM    │   │    Flow      │
               └──────┬───────┘   └──────────────┘
                      │
                      ▼
               Final Response
```

---

## Future Improvements

Possible extensions include:

- Persistent FAQ storage using PostgreSQL or SQLite.
- REST API using FastAPI.
- Web interface using React.
- Conversation history.
- User session management.
- Better semantic search using embeddings.
- Vector database integration.
- FAQ administration dashboard.
- Human-agent ticket creation.
- Conversation logging.
- Authentication and authorization.
- Feedback collection.
- Monitoring and analytics.
- Automated FAQ updates.
- Retrieval-Augmented Generation (RAG).
- Docker-based deployment.

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Python modular programming
- Data structures
- Function design
- Search algorithms
- Text processing
- TF-IDF
- Cosine similarity
- Hybrid scoring
- Confidence thresholds
- API integration
- Environment variables
- LLM prompt engineering
- Error handling
- Application architecture
- Command-line applications
- Modular project organization

---

## Project Status

```text
Task 1 — FAQ Knowledge Base       COMPLETE
Task 2 — Groq LLM Integration     COMPLETE
Task 3 — Intelligent Matching     COMPLETE
Task 4 — Helpdesk Agent           COMPLETE
```

### Overall Status

SupportAI is currently a complete working command-line FAQ helpdesk agent.

The complete flow is:

```text
Receive Question
       ↓
Search FAQ Knowledge Base
       ↓
Calculate Matching Scores
       ↓
Select Best FAQ
       ↓
Evaluate Confidence
       ↓
Generate Grounded LLM Response
       ↓
Or Escalate When Confidence Is Insufficient
```

---

## Project Purpose

SupportAI was developed as a practical learning project to demonstrate how traditional information retrieval techniques and modern LLM technology can be combined into a single application.

Instead of allowing the LLM to answer every question freely, SupportAI first searches its structured knowledge base and only uses the LLM after identifying a sufficiently relevant FAQ.

This architecture provides a foundation for building more advanced customer-support and RAG-based systems in the future.

---

## License

This project is intended for educational and practice purposes.