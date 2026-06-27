from typing import TypedDict, List, Dict


class ChatState(TypedDict):
    question: str
    messages: List[Dict[str, str]]
    intent: str
    context: str
    answer: str

from langchain_core.prompts import ChatPromptTemplate

from app.llm import get_llm
from app.memory import format_chat_history
from app.prompts import CUSTOMER_SUPPORT_PROMPT
from app.retriever import get_retriever


def classify_intent(state: ChatState) -> ChatState:
    question = state["question"]

    llm = get_llm()

    prompt = f"""
Classify the customer message into exactly one category:

support_question
human_escalation
out_of_scope

Customer message:
{question}

Return only the category.
"""

    response = llm.invoke(prompt)
    intent = response.content.strip().lower()

    if intent not in ["support_question", "human_escalation", "out_of_scope"]:
        intent = "support_question"

    state["intent"] = intent
    return state


def retrieve_context(state: ChatState) -> ChatState:
    retriever = get_retriever()

    chat_history = format_chat_history(state["messages"])
    retrieval_query = f"{chat_history}\nCurrent question: {state['question']}"

    docs = retriever.invoke(retrieval_query)
    state["context"] = "\n\n".join(doc.page_content for doc in docs)

    return state


def generate_answer(state: ChatState) -> ChatState:
    llm = get_llm()

    chat_history = format_chat_history(state["messages"])

    prompt = ChatPromptTemplate.from_template(CUSTOMER_SUPPORT_PROMPT)
    chain = prompt | llm

    response = chain.invoke(
        {
            "chat_history": chat_history,
            "context": state["context"],
            "question": state["question"],
        }
    )

    state["answer"] = response.content + "\n\n**Sources:** support_docs.txt"
    return state


def escalate_to_human(state: ChatState) -> ChatState:
    state["answer"] = (
        "I can escalate this to a human support agent. "
        "Please contact support@quickhelpstore.com with your order details."
        "\n\n**Sources:** support_docs.txt"
    )
    return state


def out_of_scope_response(state: ChatState) -> ChatState:
    state["answer"] = (
        "I can only help with QuickHelp Store support topics such as refunds, "
        "shipping, payments, account issues, and support escalation."
    )
    return state

from langgraph.graph import StateGraph, END


def route_by_intent(state: ChatState) -> str:
    if state["intent"] == "human_escalation":
        return "human_escalation"

    if state["intent"] == "out_of_scope":
        return "out_of_scope"

    return "support_question"


def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("classify_intent", classify_intent)
    graph.add_node("retrieve_context", retrieve_context)
    graph.add_node("generate_answer", generate_answer)
    graph.add_node("escalate_to_human", escalate_to_human)
    graph.add_node("out_of_scope_response", out_of_scope_response)

    graph.set_entry_point("classify_intent")

    graph.add_conditional_edges(
        "classify_intent",
        route_by_intent,
        {
            "support_question": "retrieve_context",
            "human_escalation": "escalate_to_human",
            "out_of_scope": "out_of_scope_response",
        },
    )

    graph.add_edge("retrieve_context", "generate_answer")
    graph.add_edge("generate_answer", END)
    graph.add_edge("escalate_to_human", END)
    graph.add_edge("out_of_scope_response", END)

    return graph.compile()


support_graph = build_graph()