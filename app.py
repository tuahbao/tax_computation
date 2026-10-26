import streamlit as st
import pandas as pd

st.title("Income Tax Calculator")

# Allow the user to preview the samples.
with st.expander("Preview Sample Tax Rates"):
    tax_data = {
        "Income Range ($)": [
            "Equal or Above 15,000",
            "Equal or Above 14,000",
            "Equal or Above 13,000",
            "Below 13,000"
        ],
        "Tax Rate": [
            "40%",
            "35%",
            "30%",
            "25%"
        ]
    }

    df = pd.DataFrame(tax_data)
    st.dataframe(df, use_container_width=True)

# Function to calculate tax
def cal_tax(income):
    if income >= 15000:
        tax_amt = income * 0.4
    elif income >= 14000:
        tax_amt = income * 0.35
    elif income >= 13000:
        tax_amt = income * 0.3
    else:
        tax_amt = income * 0.25
    return tax_amt

# Allow the user to enter income
income = st.number_input(
    "Enter your income ($)",
    min_value=0.0,
    step=100.0,
    format="%.2f"
)

# Calculate tax when the button is clicked
if st.button("Calculate Tax"):
    tax_amt = cal_tax(income)

    st.write(f"Your income: ${income:,.2f}")
    st.write(f"Your tax rate: {tax_amt / income:.0%}" if income > 0 else "Your tax rate: N/A")

    st.success(f"Your tax amount is ${tax_amt:,.2f}")

