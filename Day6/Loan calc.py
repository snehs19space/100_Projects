import streamlit as st
import pandas as pd
import math

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

def prepayment_schedule(principal, annual_rate, tenure_months, prepayments):
    monthly_rate = annual_rate / (12 * 100)
    emi = calculate_emi(principal, annual_rate, tenure_months)

    month = 1
    outstanding = principal
    total_interest = 0
    schedule = []

    prepay_dict = {p['month']: p['amount'] for p in prepayments}

    while outstanding > 0.1:
        interest = outstanding * monthly_rate
        principal_paid = emi - interest

        if principal_paid > outstanding:
            principal_paid = outstanding
            emi = interest + principal_paid  # final EMI adjustment

        closing = outstanding - principal_paid
        row = {
            "Month": month,
            "Opening Balance": round(outstanding, 2),
            "EMI": round(emi, 2),
            "Interest Paid": round(interest, 2),
            "Principal Paid": round(principal_paid, 2),
            "Closing Balance": round(closing, 2),
            "Prepayment": 0
        }

        # Prepayment check
        if month in prepay_dict:
            pre_amt = prepay_dict[month]
            row["Prepayment"] = pre_amt
            closing -= pre_amt
            if closing < 0:
                closing = 0

        schedule.append(row)
        total_interest += interest
        outstanding = closing
        month += 1

    return schedule, month - 1, total_interest

# Streamlit UI
st.title("Loan EMI & Prepayment Calculator")

principal = st.number_input("Loan Principal (₹)", min_value=1000, step=1000)
annual_rate = st.slider("Annual Interest Rate (%)", 5.0, 20.0, 8.5, 0.1)
tenure_years = st.slider("Loan Tenure (Years)", 1, 5, 3)
tenure_months = tenure_years * 12

num_prepayments = st.number_input("Number of Prepayments", min_value=0, max_value=5, value=0, step=1)
prepayments = []

if num_prepayments > 0:
    st.subheader("Prepayment Details")
    for i in range(num_prepayments):
        col1, col2 = st.columns(2)
        with col1:
            month = st.number_input(f"Month of Prepayment {i+1}", min_value=1, max_value=tenure_months, step=1)
        with col2:
            amount = st.number_input(f"Prepayment Amount {i+1} (₹)", min_value=1000, step=500)
        prepayments.append({"month": month, "amount": amount})

if st.button("Calculate"):
    if principal > 0:
        schedule, total_months, total_interest = prepayment_schedule(principal, annual_rate, tenure_months, prepayments)
        df = pd.DataFrame(schedule)
        st.write(f"### EMI: ₹{calculate_emi(principal, annual_rate, tenure_months):.2f}")
        st.write(f"### Loan Paid Off In: {total_months} Months")
        st.write(f"### Total Interest Paid: ₹{total_interest:.2f}")
        st.dataframe(df)
    else:
        st.warning("Please enter a valid loan amount.")
