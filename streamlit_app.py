import streamlit as st
from pathlib import Path

from app.chatbot import get_chatbot_response

st.set_page_config(
    page_title="AssistFlow AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    margin-bottom:0;
}

.subtitle{
    color:#888;
    font-size:18px;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
    margin-top:40px;
}

.stat-box{
    padding:10px;
    border-radius:10px;
    background:#f5f5f5;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------

with st.sidebar:

    st.title("🤖 AssistFlow AI")

    st.caption("Enterprise Agentic Customer Support Platform")

    st.divider()

    st.subheader("📚 Knowledge Base")

    txt_count = len(list(Path("knowledge_base/txt").glob("*.txt")))
    pdf_count = len(list(Path("knowledge_base/pdf").glob("*.pdf")))
    docx_count = len(list(Path("knowledge_base/docx").glob("*.docx")))

    st.write(f"TXT Files : {txt_count}")
    st.write(f"PDF Files : {pdf_count}")
    st.write(f"DOCX Files : {docx_count}")

    st.divider()

    st.subheader("📊 Chat Statistics")

    user_messages = sum(
        1 for m in st.session_state.messages if m["role"] == "user"
    )

    assistant_messages = sum(
        1 for m in st.session_state.messages if m["role"] == "assistant"
    )

    st.metric("User Messages", user_messages)
    st.metric("Assistant Responses", assistant_messages)

    st.divider()

    st.subheader("💡 Suggested Questions")

    st.write("• What is your refund policy?")
    st.write("• How long does shipping take?")
    st.write("• Payment failed")
    st.write("• I cannot login")
    st.write("• I want to speak to a human")

    st.divider()

    if st.button("🧹 Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------- Header ----------

st.markdown(
    '<div class="main-title">🤖 AssistFlow AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Enterprise Agentic Customer Support Platform powered by Gemini, LangGraph & RAG</div>',
    unsafe_allow_html=True,
)

# ---------- Welcome ----------

if len(st.session_state.messages) == 0:

    with st.chat_message("assistant"):

        st.markdown("""
Hello! 👋

I'm **AssistFlow AI**.

I can help you with:

- Refund Policy
- Shipping
- Payments
- Account Issues
- Human Escalation

How can I assist you today?
""")

# ---------- Previous Messages ----------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- Chat ----------

question = st.chat_input("Ask a customer support question...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("AssistFlow AI is thinking..."):

            answer = get_chatbot_response(
                question,
                messages=st.session_state.messages
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

st.markdown(
"""
<div class="footer">
AssistFlow AI • Built with Gemini • LangChain • LangGraph • ChromaDB • Streamlit
</div>
""",
unsafe_allow_html=True)