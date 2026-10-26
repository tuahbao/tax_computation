
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Income Tax Calculator & Income Predictor")

# 1. Preview sample tax rates
with st.expander("Preview Sample Tax Rates"):
    tax_data = {
        "Income Range ($)": [
            "Equal or Above 15,000",
            "Equal or Above 14,000",
            "Equal or Above 13,000",
            "Below 13,000"
        ],
        "Tax Rate": ["40%", "35%", "30%", "25%"]
    }

    df = pd.DataFrame(tax_data)
    st.dataframe(df, width="stretch")


# 2. Your original tax calculation function
def cal_tax(income):
    if income >= 15000:
        tax_amt = income * 0.40
    elif income >= 14000:
        tax_amt = income * 0.35
    elif income >= 13000:
        tax_amt = income * 0.30
    else:
        tax_amt = income * 0.25

    return tax_amt


# 3. Illustrative historical income data
# Replace these values with actual historical data
historical_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024, 2025],
    "Income": [30000, 32000, 33500, 36000, 38000]
})

st.subheader("Income History")
st.write("Example historical data used to train the model.")
st.dataframe(historical_data, width="stretch")


# 4. Let the user enter their current annual income
current_income = st.number_input(
    "Enter your income for 2026 ($)",
    min_value=0.0,
    value=40000.0,
    step=1000.0
)


# 5. Train the model and predict future income
if st.button("Predict 2027 Income & Calculate Tax"):

    # Add the user's current income to the historical data
    training_data = pd.concat([
        historical_data,
        pd.DataFrame({
            "Year": [2026],
            "Income": [current_income]
        })
    ], ignore_index=True)

    # X = input feature; y = value we want to predict
    X = training_data[["Year"]]
    y = training_data["Income"]

    # Train the machine learning model
    model = LinearRegression()
    model.fit(X, y)

    # Predict income for the next year
    next_year = pd.DataFrame({"Year": [2027]})
    predicted_income = model.predict(next_year)[0]

    # Income cannot be negative
    predicted_income = max(0, predicted_income)

    # Calculate tax on predicted income
    predicted_tax = cal_tax(predicted_income)

    # Display results
    st.subheader("Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Current Income (2026)",
            f"${current_income:,.2f}"
        )

    with col2:
        st.metric(
            "Predicted Income (2027)",
            f"${predicted_income:,.2f}"
        )

    st.success(
        f"Estimated tax on predicted income: "
        f"${predicted_tax:,.2f}"
    )

    # Show the historical trend and prediction
    chart_data = training_data.set_index("Year")
    chart_data.loc[2027] = predicted_income

    st.subheader("Historical Income & Prediction")
    st.line_chart(chart_data)
