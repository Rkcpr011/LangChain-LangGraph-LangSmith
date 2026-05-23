# 🦜 LangChain · LangGraph · LangSmith
### A hands-on, end-to-end journey from LLM basics to production-grade Agentic AI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-1C3C3C?style=flat-square&logo=chainlink)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2%2B-FF6B35?style=flat-square)
![Jupyter](https://img.shields.io/badge/Notebooks-Jupyter-F37626?style=flat-square&logo=jupyter)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 About This Repository

This repository is a **structured, hands-on learning path** covering the full LangChain ecosystem — from model invocation and prompt engineering to building stateful multi-agent systems with LangGraph.

Every folder maps to a **real concept**, built progressively — no toy examples, no shortcuts.

> Built by **Rakesh Kumar** | SDE2 @ CGI | Masters in AI/ML  
> *Turning theory into production-ready AI systems, one notebook at a time.*

---

## 🗺️ Learning Roadmap

```
LangChain Core          LangGraph Workflows         Production Patterns
─────────────           ───────────────────         ───────────────────
Model Setup             Sequential Workflow          Streaming
Prompts                 Parallel Workflow            Persistence (SQLite)
Structured Output       Conditional Routing          Short/Long-Term Memory
Output Parsers          Iterative (Loops)            Human-in-the-Loop
Chains (LCEL)           Chatbot with State           Streamlit UI
Runnables               Tools in Graphs              Resume Paused Graphs
Document Loaders        ────────────────
Text Splitters          RAG + Agents
Vector Stores           Tool Calling
Retrievers              AI Agent (ReAct)
RAG Pipeline
```

---

## 📁 Repository Structure

### 🔵 Phase 1 — LangChain Core Concepts (C0–C14)

| Folder | Concept | Key Highlights |
|--------|---------|----------------|
| `C0.Lab` | Environment Setup | API keys, `.env`, package setup |
| `C1.Model` | LLM Model Invocation | OpenAI, Groq, Anthropic via LangChain |
| `C2.Prompts` | Prompt Engineering | `ChatPromptTemplate`, `SystemMessage`, few-shot |
| `C3.WithStructuredOutput` | Structured Output | Pydantic models, `.with_structured_output()` |
| `C4.OutputParsers` | Output Parsers | `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser` |
| `C5.Chains` | LCEL Chains | Pipe operator `\|`, chain composition |
| `C6.Runnable` | Runnables | `RunnablePassthrough`, `RunnableLambda`, `RunnableParallel` |
| `C7.Document_loader` | Document Loaders | PDF, Web, Text, CSV loaders |
| `C8.TextSplitter` | Text Splitting | `RecursiveCharacterTextSplitter`, chunk strategy |
| `C9.VectorStore` | Vector Stores | FAISS, Chroma — embed, index, search |
| `C10.Retrievers` | Retrievers | Similarity search, MMR, contextual compression |
| `C11.RAG` | RAG Pipeline | Full end-to-end Retrieval-Augmented Generation |
| `C11.YoutubeChatBot` | YouTube Chatbot | Transcript loader → chunking → RAG → chat |
| `C12.Tools` | Custom Tools | `@tool` decorator, tool schemas |
| `C13.ToolCalling` | Tool Calling | LLM + bind_tools, function calling |
| `C14.AIAgentUsingLC` | ReAct Agent | `create_react_agent`, agent executor |

---

### 🟠 Phase 2 — LangGraph: Stateful Agent Workflows (C15–C26)

| Folder | Concept | Key Highlights |
|--------|---------|----------------|
| `C15.LG_sequentialWF` | Sequential Workflow | `StateGraph`, nodes, edges, `TypedDict` state |
| `C16.parallelWorkflow` | Parallel Execution | Fan-out / fan-in, concurrent node execution |
| `C17.ConditionalWorkflow` | Conditional Routing | `add_conditional_edges`, router functions |
| `C18.IterativeWorkflows` | Iterative / Loops | Cyclic graphs, self-correction loops |
| `C19.ChatBotusingLangGraph` | Stateful Chatbot | Full chatbot with message history in state |
| `C20.Persistence` | Checkpointing | `MemorySaver`, conversation persistence |
| `C21.ChatBotUIwithST` | Streamlit UI | Production chatbot UI with streaming |
| `C22.Streaming` | Token Streaming | `.astream()`, `stream_mode`, real-time output |
| `C23.ResumeChat` | Human-in-the-Loop | `interrupt_before`, graph resume, approval flow |
| `C24.Langraph_SQLite` | SQLite Persistence | `SqliteSaver` as persistent checkpointer |
| `C25.ToolsInLG` | Tools in LangGraph | ToolNode, tool routing inside graph |
| `C26.STMLTMPersistent` | Memory Management | Short-term (in-graph) + Long-term (external) memory |

---

## 🚀 Featured Projects

### 1. 🎥 YouTube Chatbot (`C11.YoutubeChatBot`)
A RAG-based chatbot that answers questions from any YouTube video.
- YouTube transcript extraction → chunking → FAISS indexing → conversational QA
- Stack: `LangChain` + `FAISS` + `OpenAI Embeddings`

### 2. 🤖 AI Agent with ReAct (`C14.AIAgentUsingLC`)
A tool-using AI agent built with the ReAct (Reasoning + Acting) pattern.
- Custom tool definitions, LLM reasoning over tools, agent executor
- Stack: `LangChain Agents` + `Tavily Search` + `OpenAI`

### 3. 🔄 Self-Correcting RAG (`C18.IterativeWorkflows`)
A LangGraph workflow that loops and self-corrects until quality threshold is met.
- Implements the Corrective RAG / Self-RAG concept
- Stack: `LangGraph` cyclic graph + `Grader nodes` + `Retriever`

### 4. 💬 Production Chatbot with UI (`C21.ChatBotUIwithST`)
Full-stack conversational AI with persistent memory and a Streamlit UI.
- Streaming responses, session-based memory, clean chat interface
- Stack: `LangGraph` + `Streamlit` + `SQLite Checkpointer`

### 5. 🧠 Human-in-the-Loop Agent (`C23.ResumeChat`)
An agent that pauses for human approval before taking sensitive actions.
- `interrupt_before` → human review → `graph.invoke` resume
- Stack: `LangGraph` + `MemorySaver` + interrupt mechanism

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- OpenAI / Groq API key (or any supported LLM provider)

### Installation

```bash
# Clone the repo
git clone https://github.com/Rkcpr011/LangChain-LangGraph-LangSmith.git
cd LangChain-LangGraph-LangSmith

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install langchain langgraph langchain-openai langchain-community
pip install faiss-cpu chromadb streamlit python-dotenv
pip install langchain-groq tavily-python
```

### Environment Setup

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=LangChain-LangGraph-Practice
```

---

## 🧠 Core Concepts Quick Reference

### LangChain — LCEL Chain
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Answer this: {question}")
model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model | StrOutputParser()

chain.invoke({"question": "What is RAG?"})
```

### LangGraph — Basic StateGraph
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    message: str

def node_one(state: State):
    return {"message": state["message"] + " → processed"}

graph = StateGraph(State)
graph.add_node("process", node_one)
graph.set_entry_point("process")
graph.add_edge("process", END)

app = graph.compile()
app.invoke({"message": "Hello"})
```

### LangGraph — Conditional Routing
```python
def router(state: State):
    if state["score"] > 0.7:
        return "good_path"
    return "retry_path"

graph.add_conditional_edges("grade_node", router, {
    "good_path": "answer_node",
    "retry_path": "retrieve_node"
})
```

---

## 🏭 Tech Stack

| Category | Tools |
|----------|-------|
| LLM Providers | OpenAI, Groq, Anthropic |
| Orchestration | LangChain (LCEL), LangGraph |
| Observability | LangSmith |
| Vector Stores | FAISS, Chroma |
| Embeddings | OpenAI `text-embedding-3-small` |
| Document Loaders | PyPDF, WebBaseLoader, YoutubeLoader |
| Persistence | SQLite (`SqliteSaver`), In-memory |
| UI | Streamlit |
| Language | Python 3.10+ |
| Notebooks | Jupyter |

---

## 📊 Progress Tracker

- [x] LangChain Core (Models, Prompts, Chains)
- [x] RAG Pipeline (Loader → Splitter → VectorStore → Retriever → RAG)
- [x] Tool Creation & Tool Calling
- [x] ReAct Agent
- [x] LangGraph Workflows (Sequential, Parallel, Conditional, Iterative)
- [x] Persistence & Memory (MemorySaver, SQLite)
- [x] Human-in-the-Loop
- [x] Streaming
- [ ] LangSmith Tracing & Evaluation *(coming soon)*
- [ ] LangGraph Platform Deployment *(coming soon)*

---

## 🎯 Interview Prep Notes

Key concepts frequently asked in GenAI / ML Engineer interviews covered in this repo:

- **RAG vs Fine-tuning** — when to use which (C11)
- **LCEL vs Legacy Chains** — why LCEL is the modern standard (C5, C6)
- **ReAct Pattern** — reasoning + acting loop in agents (C14)
- **Graph-based Agent Orchestration** — why LangGraph over simple chains (C15–C18)
- **Memory in LLMs** — short-term vs long-term, checkpointing (C20, C26)
- **Streaming** — how token-by-token output works in production (C22)
- **Human-in-the-Loop** — interrupt, review, resume pattern (C23)

---

## 👤 Author

**Rakesh Kumar**  
SDE2 @ CGI | Masters in AI/ML  

[![GitHub](https://img.shields.io/badge/GitHub-Rkcpr011-181717?style=flat-square&logo=github)](https://github.com/Rkcpr011)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> *"The best way to learn agentic AI is to build it — one graph node at a time."*
