# AI Interview Simulator

A Generative AI–powered application that simulates a **realistic interview cycle** by generating role-specific questions, evaluating candidate answers, and providing structured feedback.

This project focuses on **system design, LLM control, and explainability**, rather than feature bloat.

---

## 🔍 Problem Statement

Candidates often lack access to structured interview practice that provides:
- Context-aware questions  
- Objective evaluation  
- Actionable feedback  

Most existing tools either:
- Only generate questions, or  
- Provide unstructured, generic feedback  

This project addresses that gap by modeling a **single interview cycle** with clear separation between **question generation, evaluation, and feedback**.

---

## ✅ Solution Overview

The AI Interview Simulator implements a **controller + agent-based architecture** where each component has a single responsibility:

- Generate an interview question based on role and difficulty
- Evaluate the candidate’s answer using a structured rubric
- Convert evaluation into clear, user-friendly feedback

The system is intentionally scoped to **one complete interview cycle** to prioritize depth, correctness, and explainability.

---

## 🧠 Architecture

Controller (main/app)
        ↓
Question Generator Agent
        ↓
Evaluation Agent
        ↓
Feedback Agent
        ↓
LLM Client (Groq API)


### Design Principles
- Separation of concerns  
- Reusable LLM abstraction  
- Prompt-controlled agent behavior  
- Explainable evaluation flow  

---

## 🧩 Components & Responsibilities

### `main.py`
- CLI controller for the interview flow
- Handles user input and output
- Orchestrates agent execution

### `app.py`
- Streamlit-based web interface
- UI layer only (no AI logic)
- Calls underlying agents

### `core/llm_client.py`
- Centralized communication with the LLM
- Abstracts Groq API usage
- Keeps the system model-agnostic

### `agents/question_agent.py`
- Generates role- and difficulty-specific interview questions

### `agents/evaluation_agent.py`
- Evaluates candidate answers
- Produces structured output (score, strengths, gaps)

### `agents/feedback_agent.py`
- Converts raw evaluation into actionable feedback

---

## 🔄 Runtime Flow

1. User selects role and difficulty  
2. Question Generator Agent creates an interview question  
3. User submits an answer  
4. Evaluation Agent scores and analyzes the answer  
5. Feedback Agent generates improvement guidance  
6. One complete interview cycle is completed  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Groq API (LLM backend)  
- LLaMA-based models  
- Modular agent-based architecture  

---

## 🌐 Deployment

The application is deployed on **Streamlit Cloud**.

- Source code is hosted on GitHub  
- API keys are managed using environment secrets  
- No sensitive data is hardcoded  

---

## 🎯 Scope & Design Decisions

### Why only one interview question?
The project intentionally focuses on a **single interview cycle** to:
- Ensure high-quality evaluation logic  
- Maintain explainability  
- Avoid shallow multi-feature implementation  

The architecture is **fully extensible** and can support:
- Multi-round interviews  
- Session memory  
- Adaptive difficulty  
- Persistent scoring  

---

## ⚠️ Limitations

- Single-question interview cycle  
- No long-term session memory  
- No database persistence  
- Evaluation quality depends on LLM reasoning  

These are **explicit design trade-offs**, not oversights.

---

## 🚀 Future Enhancements

- Multi-round interview sessions  
- Adaptive difficulty based on performance  
- Session-level scoring and analytics  
- Interview-type customization (HR, system design, DSA)  
- Persistent user profiles  

---

## 🧠 Key Takeaway

This project demonstrates how to **design, control, and deploy a Generative AI system for evaluation tasks**, not just text generation.

It emphasizes:
- Architecture over UI  
- Depth over feature count  
- Explainability over black-box behavior  

---

## 👤 Author

**Aryan Nigam**  
B.Tech CSE | Generative AI & Backend Systems
