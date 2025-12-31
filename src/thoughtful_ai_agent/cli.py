from __future__ import annotations

import re

import typer

_QA_PAIRS = [
    (
        "What does the eligibility verification agent (EVA) do?",
        "EVA automates the process of verifying a patient's eligibility and benefits "
        "information in real-time, eliminating manual data entry errors and reducing "
        "claim rejections.",
    ),
    (
        "What does the claims processing agent (CAM) do?",
        "CAM streamlines the submission and management of claims, improving accuracy, "
        "reducing manual intervention, and accelerating reimbursements.",
    ),
    (
        "How does the payment posting agent (PHIL) work?",
        "PHIL automates the posting of payments to patient accounts, ensuring fast, "
        "accurate reconciliation of payments and reducing administrative burden.",
    ),
    (
        "Tell me about Thoughtful AI's Agents.",
        "Thoughtful AI provides a suite of AI-powered automation agents designed to "
        "streamline healthcare processes. These include Eligibility Verification (EVA), "
        "Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    ),
    (
        "What are the benefits of using Thoughtful AI's agents?",
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, "
        "improve operational efficiency, and reduce errors in critical processes like "
        "claims management and payment posting.",
    ),
]


def _normalize_question(question: str) -> str:
    cleaned = question.strip().lower()
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"[?.!]+$", "", cleaned)
    return cleaned


_QA_MAP = {_normalize_question(question): answer for question, answer in _QA_PAIRS}


def answer_question(question: str) -> str:
    """Return the hardcoded response for a matching question."""
    normalized = _normalize_question(question)
    return _QA_MAP.get(
        normalized,
        "I'm sorry, I don't have an answer for that question. "
        "Please ask about Thoughtful AI's agents.",
    )


app = typer.Typer(help="Answer common questions about Thoughtful AI.")


@app.command()
def ask(question: str = typer.Argument(..., help="Question to answer.")) -> None:
    typer.echo(answer_question(question))


def main() -> None:
    app()


if __name__ == "__main__":
    main()
