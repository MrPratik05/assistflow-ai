def format_chat_history(messages):
    """
    Converts chat messages into a readable conversation history
    for the LLM prompt.
    """

    if not messages:
        return "No previous conversation."

    formatted_messages = []

    for message in messages:
        role = message.get("role", "user")
        content = message.get("content", "")

        if role == "user":
            formatted_messages.append(f"Customer: {content}")
        else:
            formatted_messages.append(f"Assistant: {content}")

    return "\n".join(formatted_messages)