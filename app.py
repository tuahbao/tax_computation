import streamlit as st
import pandas as pd


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

tax1 = cal_tax(15000)
tax2 = cal_tax(14000)
tax3 = cal_tax(13000)
tax4 = cal_tax(12000)

print(tax1)
print(tax2)
print(tax3)
print(tax4)
