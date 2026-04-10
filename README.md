# 🎯 AI Interview Simulator

A **Generative AI-powered interview practice system** that simulates realistic technical interviews by generating role-specific questions, evaluating candidate answers against structured rubrics, and providing actionable feedback.

Unlike generic chatbots, this system enforces **consistent evaluation criteria**, **explainable scoring**, and **separation of concerns** between question generation, evaluation, and feedback.

---

## 🚀 Live Demo

**Deployment Link:** [Your Streamlit URL Here]

---

## 🔥 Key Highlights

- 🎯 **Role-specific questions** - Tailored for Backend, Frontend, Data Science, DevOps roles
- 📊 **Structured evaluation** - 4-dimension rubric (Technical Accuracy, Completeness, Clarity, Communication)
- 💬 **Actionable feedback** - Specific strengths, gaps, and improvement suggestions
- 🧠 **LLM-powered** - Uses Groq's LLaMA 3.1 for reliable, fast generation
- 🔍 **Explainable scoring** - Every score comes with a justification
- 🧱 **Modular architecture** - Clean separation: Controller → Agents → LLM Client
- 🎨 **Dual interface** - CLI (main.py) + Web UI (Streamlit)

---

## 🔍 Problem Statement

Candidates often lack access to structured interview practice that provides:
- **Context-aware questions** relevant to their target role
- **Objective evaluation** against consistent standards
- **Actionable feedback** they can actually use to improve

Most existing tools either:
- ❌ Only generate questions without evaluation
- ❌ Provide unstructured, generic feedback ("Good answer!")
- ❌ Have no consistent scoring criteria

**This project solves that** by modeling a complete interview cycle with clear separation between question generation, evaluation, and feedback.

---

## 🏗️ System Architecture

```
User Input (Role + Difficulty)
         ↓
┌─────────────────┐
│ Question Agent  │ → Generates role-specific question
└─────────────────┘
         ↓
   User Answer
         ↓
┌─────────────────┐
│ Evaluation Agent│ → Scores against 4 rubrics (0-5 each)
└─────────────────┘
         ↓
┌─────────────────┐
│  Feedback Agent │ → Converts scores to actionable advice
└─────────────────┘
         ↓
   Session Summary
```

---

## 📊 Evaluation Rubric

| Criterion | Score Range | Description |
|-----------|-------------|-------------|
| **Technical Accuracy** | 0-5 | Correctness of concepts and reasoning |
| **Completeness** | 0-5 | Coverage of key aspects |
| **Clarity & Structure** | 0-5 | Logical flow and articulation |
| **Communication Quality** | 0-5 | Conciseness and relevance |

**Total:** 0-20 → 0-100%

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Web UI | Streamlit |
| LLM | Groq API (LLaMA 3.1-8B Instant) |
| Architecture | Agent-based |

---

## 📁 Project Structure

```
AI-Interview-Simulator/
├── agents/
│   ├── question_agent.py      # Generates questions
│   ├── evaluation_agent.py    # Scores answers
│   └── feedback_agent.py      # Creates feedback
├── core/
│   ├── llm_client.py          # Groq API wrapper
│   └── prompts.py             # Prompt templates
├── main.py                    # CLI entry point
├── app.py                     # Web entry point
├── requirements.txt
└── .env                       # API key
```

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/AryanNigam123/AI-Interview-Simulator.git
cd AI-Interview-Simulator
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set API Key
```bash
echo "GROQ_API_KEY=your_key_here" > .env
```

### 3. Run
```bash
# CLI Mode
python main.py

# Web Mode
streamlit run app.py
```

---

## 📖 Usage Example

```bash
$ python main.py

Select Role: 1 (Backend Developer)
Select Difficulty: 2 (Medium)

📝 Question: "Explain how indexing works in databases and its trade-offs."

Your answer: Indexes speed up reads but slow down writes...

📊 Scores:
- Technical Accuracy: 4/5
- Completeness: 3/5
- Clarity: 4/5
- Communication: 4/5

💡 Feedback: Strong technical foundation. Include write-performance trade-offs next time.

Total Score: 15/20 (75%)
```

---

## ⚙️ Configuration

Edit `core/prompts.py`:
```python
MODEL_NAME = "llama3-8b-8192"
TEMPERATURE = 0.3
PASSING_SCORE = 14  # 70%
```

---

## 🚧 Limitations

- Single question per session (by design)
- No session persistence
- Text-only answers
- 4 roles currently supported

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| API key error | Check .env file |
| Rate limit | Wait 2 minutes |
| Import error | `pip install -r requirements.txt` |

---

## 📄 License

MIT License - Free for personal and commercial use

---

## 👤 Author

**Aryan Nigam** - B.Tech CSE | Generative AI & Backend Systems
- GitHub: [@AryanNigam123](https://github.com/AryanNigam123)

---

## ⭐ Support

Star the repo if this helped you practice interviews!

---

**Built with ❤️ to help candidates succeed** | April 2026
