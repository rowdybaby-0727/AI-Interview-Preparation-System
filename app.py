import streamlit as st
import random

from questions import questions
from evaluator import evaluate_answer

st.set_page_config(
    page_title="AI Interview Preparation System",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 AI Interview Preparation System")

st.write("Practice HR and Technical Interview Questions")

category = st.selectbox(
    "Select Interview Category",
    list(questions.keys())
)

if st.button("Generate Question"):

    selected = random.choice(questions[category])

    st.session_state.question = selected["question"]
    st.session_state.answer = selected["answer"]

if "question" in st.session_state:

    st.subheader("Interview Question")

    st.info(st.session_state.question)

    user_answer = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        score = evaluate_answer(
            user_answer,
            st.session_state.answer
        )

        st.success(f"Your Score: {score}%")

        if score > 75:
            st.success("Excellent Answer")
        elif score > 50:
            st.warning("Good Answer")
        else:
            st.error("Need Improvement")