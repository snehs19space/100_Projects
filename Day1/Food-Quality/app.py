import streamlit as st

def check_food_quality(score):
    if score > 50:
        return "Good Quality", "green"
    else:
        return "Bad Quality", "red"

st.title("🍽️ Food Quality Checker")

score = st.slider("Select food quality score", 0, 100, 50)

result_text, color = check_food_quality(score)

st.markdown(f"<h3 style='color:{color}'>Food is of {result_text}</h3>", unsafe_allow_html=True)
