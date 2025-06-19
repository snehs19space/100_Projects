import streamlit as st

def check_food_quality(score):
    if score > 50:
        return "Good Quality"
    else:
        return "Bad Quality"

st.title("Food Quality Checker")

score = st.slider("Select food quality score", 0, 100, 50)

result = check_food_quality(score)

st.subheader(f"Food is of {result}")
