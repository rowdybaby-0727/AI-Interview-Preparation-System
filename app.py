import streamlit as st
import random

# PAGE CONFIG
st.set_page_config(
    page_title="AI Interview Preparation System",
    page_icon="🎯",
    layout="centered"
)

# TITLE
st.title("🎯 AI Interview Preparation System")

st.write("Practice technical interview questions with AI.")

# QUESTION DATASET
questions = {
    "Python": {
        "Easy": [
            "What is Python?",
            "What are lists in Python?",
            "Difference between list and tuple?"
        ],
        "Medium": [
            "Explain OOPs concepts in Python.",
            "What is inheritance?",
            "Explain decorators in Python."
        ],
        "Hard": [
            "Explain multithreading in Python.",
            "What is GIL in Python?",
            "Explain generators and iterators."
        ]
    },

    "Cloud Computing": {
        "Easy": [
            "What is Cloud Computing?",
            "Types of cloud deployment models?",
            "What is virtualization?"
        ],
        "Medium": [
            "Explain IaaS, PaaS, SaaS.",
            "What is load balancing?",
            "What is auto scaling?"
        ],
        "Hard": [
            "Explain Docker and Kubernetes.",
            "What is serverless computing?",
            "Explain cloud security challenges."
        ]
    },

    "Machine Learning": {
        "Easy": [
            "What is Machine Learning?",
            "Difference between AI and ML?",
            "What is supervised learning?"
        ],
        "Medium": [
            "Explain Random Forest.",
            "What is overfitting?",
            "Difference between classification and regression?"
        ],
        "Hard": [
            "Explain deep learning.",
            "What is gradient descent?",
            "Explain neural networks."
        ]
    },

    "HR Questions": {
        "Easy": [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?"
        ],
        "Medium": [
            "Describe a challenge you faced.",
            "Where do you see yourself in 5 years?",
            "Why do you want this job?"
        ],
        "Hard": [
            "How do you handle pressure?",
            "Explain a leadership situation.",
            "Describe a failure and what you learned."
        ]
    }
}

# SELECT DOMAIN
domain = st.selectbox(
    "Select Interview Domain",
    list(questions.keys())
)

# SELECT LEVEL
difficulty = st.selectbox(
    "Select Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

# GENERATE BUTTON
if st.button("Generate Question"):

    selected_question = random.choice(
        questions[domain][difficulty]
    )

    st.success("Interview Question Generated!")

    st.subheader("🧠 Question:")

    st.write(selected_question)

# ANSWER SECTION
st.subheader("✍ Your Answer")

user_answer = st.text_area(
    "Type your answer here..."
)

if st.button("Submit Answer"):

    if user_answer.strip() == "":
        st.warning("Please enter your answer.")
    else:
        st.success("Answer Submitted Successfully!")

        word_count = len(user_answer.split())

        st.write(f"Word Count: {word_count}")

        if word_count < 20:
            st.error("Answer is too short.")
        elif word_count < 50:
            st.warning("Answer can be improved.")
        else:
            st.success("Good Answer Length!")

# FOOTER
st.markdown("---")
st.write("Developed by Prasanna R 🚀")