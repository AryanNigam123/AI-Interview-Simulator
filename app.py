import streamlit as st
from agents.question_agent import generate_question
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Interview Simulator",
    layout="centered"
)

# --------------------------------------------------
# Minimal CSS (readability only)
# --------------------------------------------------
st.markdown("""
<style>
    body {
        background-color: #fafafa;
        color: #1f1f1f;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    textarea {
        font-size: 0.95rem !important;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar (Neutral, technical)
# --------------------------------------------------
with st.sidebar:
    st.header("About")
    st.write(
        "This application simulates interview scenarios using a "
        "Generative AI backend. It generates role-specific questions, "
        "evaluates answers, and provides structured feedback."
    )

    st.markdown("---")
    st.caption("Architecture: Controller + Agent-based LLM design")

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("AI Interview Simulator")
st.caption(
    "A lightweight application for practicing interview questions "
    "with AI-based evaluation"
)
st.divider()

# --------------------------------------------------
# Interview Setup
# --------------------------------------------------
st.subheader("Interview Setup")

col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "Role",
        ["Software Engineer", "AI Engineer", "Backend Developer"]
    )

with col2:
    difficulty = st.selectbox(
        "Difficulty",
        ["easy", "medium", "hard"]
    )

st.divider()

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "question" not in st.session_state:
    st.session_state.question = None
if "evaluation" not in st.session_state:
    st.session_state.evaluation = None
if "feedback" not in st.session_state:
    st.session_state.feedback = None

# --------------------------------------------------
# Generate Question
# --------------------------------------------------
if st.button("Generate Interview Question", use_container_width=True):
    st.session_state.question = generate_question(role, difficulty)
    st.session_state.evaluation = None
    st.session_state.feedback = None

# --------------------------------------------------
# Question + Answer
# --------------------------------------------------
if st.session_state.question:
    st.subheader("Interview Question")
    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer",
        height=160,
        placeholder="Type your answer here..."
    )

    if st.button("Submit Answer", use_container_width=True):
        st.session_state.evaluation = evaluate_answer(
            st.session_state.question,
            answer
        )
        st.session_state.feedback = generate_feedback(
            st.session_state.evaluation
        )

# --------------------------------------------------
# Evaluation Output
# --------------------------------------------------
if st.session_state.evaluation:
    st.subheader("Evaluation")
    st.text(st.session_state.evaluation)

# --------------------------------------------------
# Feedback Output
# --------------------------------------------------
if st.session_state.feedback:
    st.subheader("Feedback")
    st.text(st.session_state.feedback)
