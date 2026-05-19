import streamlit as st
import random
from difflib import SequenceMatcher
import speech_recognition as sr
import time
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Interview Preparation System",
    page_icon="🎯",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🎯 AI Interview Preparation System")

st.write("Practice Technical Interviews with AI")

# -----------------------------------
# QUESTION DATABASE
# -----------------------------------

questions = {
    "Python": {
        "What is Python?":
        "Python is a high-level programming language used for AI, web development and automation.",

        "Explain OOPs concepts in Python.":
        "OOP concepts include encapsulation, inheritance, polymorphism and abstraction.",

        "What is GIL in Python?":
        "GIL stands for Global Interpreter Lock which allows only one thread to execute at a time."
    },

    "Cloud Computing": {
        "What is Cloud Computing?":
        "Cloud computing provides servers, storage and software over the internet.",

        "Explain IaaS, PaaS and SaaS.":
        "IaaS provides infrastructure, PaaS provides platform and SaaS provides software."
    },

    "Machine Learning": {
        "What is Machine Learning?":
        "Machine Learning allows systems to learn from data without explicit programming.",

        "What is overfitting?":
        "Overfitting occurs when a model performs well on training data but poorly on new data."
    },

    "HR Questions": {
        "Tell me about yourself.":
        "I am a Computer Science student passionate about AI, Cloud Computing and Web Development.",

        "Why should we hire you?":
        "I am hardworking, quick learner and passionate about solving real-world problems."
    }
}

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("⚙ Interview Settings")

domain = st.sidebar.selectbox(
    "Select Domain",
    list(questions.keys())
)

difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

# -----------------------------------
# RANDOM QUESTION
# -----------------------------------

question = random.choice(list(questions[domain].keys()))

st.subheader("🧠 Interview Question")

st.info(question)

# -----------------------------------
# TIMER SYSTEM
# -----------------------------------

st.subheader("⏳ Mock Interview Timer")

minutes = st.slider(
    "Set Timer (Minutes)",
    1,
    5,
    2
)

if st.button("Start Timer"):

    seconds = minutes * 60

    timer_placeholder = st.empty()

    while seconds >= 0:

        mins = seconds // 60
        secs = seconds % 60

        timer_placeholder.warning(
            f"Time Left: {mins:02d}:{secs:02d}"
        )

        time.sleep(1)

        seconds -= 1

    st.error("Time Up!")

# -----------------------------------
# ANSWER INPUT
# -----------------------------------

st.subheader("✍ Type Your Answer")

user_answer = st.text_area(
    "Write your answer here..."
)

# -----------------------------------
# VOICE INPUT
# -----------------------------------

st.subheader("🎤 Voice Input")

if st.button("Start Voice Recording"):

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            st.info("Listening... Speak Now")

            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            st.success("Voice Recognized Successfully")

            st.write("### Recognized Text")

            st.write(text)

            user_answer = text

    except:
        st.error("Microphone Error or Voice Not Clear")

# -----------------------------------
# EVALUATION
# -----------------------------------

if st.button("Evaluate Answer"):

    if user_answer.strip() == "":
        st.warning("Please enter your answer.")

    else:

        ideal_answer = questions[domain][question]

        similarity = SequenceMatcher(
            None,
            user_answer.lower(),
            ideal_answer.lower()
        ).ratio()

        score = round(similarity * 100)

        st.subheader("📊 AI Evaluation Result")

        st.metric("Score", f"{score}/100")

        # FEEDBACK
        if score >= 80:
            st.success("Excellent Answer!")
        elif score >= 60:
            st.warning("Good Answer. Can improve more.")
        else:
            st.error("Needs Improvement.")

        # WORD COUNT
        word_count = len(user_answer.split())

        st.write(f"### Word Count: {word_count}")

        # IDEAL ANSWER
        with st.expander("View Ideal Answer"):
            st.write(ideal_answer)

        # AI FEEDBACK
        st.subheader("💡 AI Suggestions")

        suggestions = []

        if word_count < 20:
            suggestions.append("Increase answer length.")

        if score < 60:
            suggestions.append("Add more technical explanation.")

        if domain == "Cloud Computing":
            if "cloud" not in user_answer.lower():
                suggestions.append("Mention cloud-related concepts.")

        if domain == "Python":
            if "python" not in user_answer.lower():
                suggestions.append("Include Python keywords.")

        if len(suggestions) == 0:
            st.success("Professional Answer.")
        else:
            for s in suggestions:
                st.write("✅", s)

        # -----------------------------------
        # PERFORMANCE DASHBOARD
        # -----------------------------------

        st.subheader("📈 Performance Dashboard")

        data = {
            "Metric": [
                "Answer Score",
                "Word Count",
                "Technical Accuracy"
            ],

            "Value": [
                score,
                word_count,
                f"{score}%"
            ]
        }

        df = pd.DataFrame(data)

        st.table(df)

        # -----------------------------------
        # WEAK AREA ANALYSIS
        # -----------------------------------

        st.subheader("⚠ Weak Area Analysis")

        weak_areas = []

        if score < 60:
            weak_areas.append("Technical Concepts")

        if word_count < 20:
            weak_areas.append("Communication Skills")

        if len(weak_areas) == 0:
            st.success("No major weak areas detected.")
        else:
            for area in weak_areas:
                st.write("❌", area)

        # -----------------------------------
        # ATS STYLE SCORE
        # -----------------------------------

        st.subheader("📄 ATS Style Score")

        ats_score = min(score + 10, 100)

        st.progress(ats_score / 100)

        st.write(f"ATS Score: {ats_score}/100")

        # -----------------------------------
        # PROGRESS TRACKING
        # -----------------------------------

        st.subheader("🚀 Progress Tracking")

        if score >= 80:
            st.success("Interview Ready")
        elif score >= 60:
            st.warning("Need More Practice")
        else:
            st.error("Beginner Level")

# -----------------------------------
# RESUME BASED QUESTIONS
# -----------------------------------

st.subheader("📂 Resume Based Interview")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "txt"]
)

if uploaded_file is not None:

    st.success("Resume Uploaded Successfully")

    st.write("Sample Resume-Based Questions:")

    st.write("• Explain your projects.")
    st.write("• What technologies have you used?")
    st.write("• Describe your internship experience.")
    st.write("• Explain your Machine Learning project.")

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.write("Developed by Prasanna R 🚀")