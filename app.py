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
# Sidebar
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
    "Practice interview questions with AI-based evaluation "
    "and actionable feedback"
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
# Session State Initialization
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
# Question & Answer Section
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
# Evaluation Output (CLEAN DISPLAY)
# --------------------------------------------------
if st.session_state.evaluation:
    eval_data = st.session_state.evaluation

    st.subheader("Evaluation")

    st.write(f"**Technical Accuracy:** {eval_data['technical_accuracy']} / 5")
    st.write(f"**Completeness:** {eval_data['completeness']} / 5")
    st.write(f"**Clarity:** {eval_data['clarity']} / 5")
    st.write(f"**Communication:** {eval_data['communication']} / 5")

    st.markdown("**Strengths**")
    st.write(eval_data["strengths"])

    st.markdown("**Gaps**")
    st.write(eval_data["gaps"])

# --------------------------------------------------
# Feedback Output (MARKDOWN RENDERED)
# --------------------------------------------------
if st.session_state.feedback:
    st.subheader("Feedback")
    st.markdown(st.session_state.feedback["overall_summary"])
