def detect_intent(question: str) -> str:
    """
    Detects the user's intent.
    Returns:
    - human_escalation
    - support_question
    """

    escalation_phrases = [
        "human",
        "agent",
        "representative",
        "real person",
        "speak to someone",
        "manager",
        "complaint",
        "escalate",
    ]

    question_lower = question.lower()

    if any(phrase in question_lower for phrase in escalation_phrases):
        return "human_escalation"

    return "support_question"