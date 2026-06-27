from app.graph import support_graph


def get_chatbot_response(question: str, messages=None):

    if messages is None:
        messages = []

    result = support_graph.invoke(
        {
            "question": question,
            "messages": messages,
            "intent": "",
            "context": "",
            "answer": "",
        }
    )

    return result["answer"]