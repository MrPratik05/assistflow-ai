# 🤖 AssistFlow AI

### Enterprise Agentic Customer Support Platform powered by Gemini, LangChain, LangGraph & RAG

AssistFlow AI is an enterprise-grade customer support platform that uses Retrieval-Augmented Generation (RAG) and agentic AI workflows to answer customer queries using company knowledge bases.

The platform combines Google's Gemini 2.5 Flash model with LangChain, LangGraph, ChromaDB, and Hugging Face Embeddings to deliver accurate, context-aware responses while supporting conversation memory, intent routing, and human escalation.

---

## 🚀 Features

- 💬 AI-powered customer support chatbot
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini 2.5 Flash integration
- 🔗 LangChain orchestration
- 🕸️ LangGraph agent workflow
- 📚 ChromaDB vector database
- 🔍 Semantic search using Hugging Face embeddings
- 💭 Conversation memory
- 🎯 Intent classification
- 🙋 Human support escalation
- 📄 Multi-format knowledge base (TXT, PDF, DOCX)
- 🌐 Interactive Streamlit web application

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit Chat UI
 │
 ▼
LangGraph Workflow
 ├── Intent Classification
 ├── Human Escalation Route
 ├── Out-of-Scope Route
 └── Support Question Route
       │
       ▼
   ChromaDB Retriever
       │
       ▼
   Knowledge Base
   TXT / PDF / DOCX
       │
       ▼
   Gemini 2.5 Flash
       │
       ▼
   Final Response + Source Citation

   ## 🏗️ Architecture

```text
                    +----------------------+
                    |      User            |
                    +----------+-----------+
                               |
                               v
                  +--------------------------+
                  |     Streamlit UI         |
                  +------------+-------------+
                               |
                               v
                  +--------------------------+
                  |   LangGraph Workflow     |
                  +------------+-------------+
                               |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
 Intent Classification   Human Escalation    Out-of-Scope Detection
                               |
                               v
                  +--------------------------+
                  |      RAG Pipeline        |
                  +------------+-------------+
                               |
                               v
                  +--------------------------+
                  |      ChromaDB            |
                  |   Vector Database        |
                  +------------+-------------+
                               |
                               v
                  +--------------------------+
                  | Knowledge Base           |
                  | TXT | PDF | DOCX         |
                  +------------+-------------+
                               |
                               v
                  +--------------------------+
                  | Gemini 2.5 Flash         |
                  +------------+-------------+
                               |
                               v
                  +--------------------------+
                  | AI Response              |
                  +--------------------------+
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| LLM | Google Gemini 2.5 Flash |
| AI Framework | LangChain |
| Workflow Engine | LangGraph |
| Vector Database | ChromaDB |
| Embeddings | Hugging Face Sentence Transformers |
| Frontend | Streamlit |
| Knowledge Base | TXT, PDF, DOCX |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
assistflow-ai/
│
├── app/
│   ├── chatbot.py
│   ├── config.py
│   ├── embeddings.py
│   ├── graph.py
│   ├── intent.py
│   ├── llm.py
│   ├── loader.py
│   ├── memory.py
│   ├── prompts.py
│   ├── retriever.py
│   └── vectorstore.py
│
├── knowledge_base/
│   ├── pdf/
│   ├── docx/
│   └── txt/
│
├── tests/
│
├── build_vectorstore.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MrPratik05/assistflow-ai.git
cd assistflow-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Build the vector database:

```bash
python build_vectorstore.py
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 🌟 Key Capabilities

- Enterprise RAG architecture
- Semantic document retrieval
- Multi-document support (TXT, PDF, DOCX)
- Conversation memory
- Intent classification
- Human escalation workflow
- Out-of-scope detection
- Modular AI architecture
- Interactive Streamlit interface
- Easily extensible knowledge base

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MrPratik05/assistflow-ai.git
cd assistflow-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Build the vector database:

```bash
python build_vectorstore.py
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 🌟 Key Capabilities

- Enterprise RAG architecture
- Semantic document retrieval
- Multi-document support (TXT, PDF, DOCX)
- Conversation memory
- Intent classification
- Human escalation workflow
- Out-of-scope detection
- Modular AI architecture
- Interactive Streamlit interface
- Easily extensible knowledge base

---

## 🔮 Future Improvements

- Admin dashboard for knowledge base management
- PDF upload directly from the web interface
- Authentication and role-based access
- Conversation analytics dashboard
- Streaming AI responses
- Docker deployment
- CI/CD with GitHub Actions
- Cloud deployment (Hugging Face Spaces / Azure / AWS)
- Multi-language customer support
- Voice-based customer support

---
## 📸 Application Preview

### Home Page

![Home Page](assets/home.png)

### AI Chat Example

![Chat Demo](assets/chat_demo.png)


---

## 👨‍💻 Author

**Pratik Patil**

MSc Artificial Intelligence | AI Engineer | Generative AI | Machine Learning

- GitHub: https://github.com/MrPratik05
- LinkedIn: https://github.com/MrPratik05/assistflow-ai

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.
