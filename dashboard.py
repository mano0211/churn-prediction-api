import streamlit as st
import requests
import json

# ------------------------------------------------------------------------
# 1. CONFIGURE THE APP
# ------------------------------------------------------------------------
st.set_page_config(page_title="Churn Predictor", page_icon="📉")

st.title("📉 Customer Churn Prediction Tool")
st.write("Enter customer details below to predict if they will cancel their service.")

# REPLACE THIS WITH YOUR RENDER URL (Keep the /predict at the end)
# Example: "https://churn-api-portfolio.onrender.com/predict"
API_URL = "https://churn-api-portfolio.onrender.com/predict"

# ------------------------------------------------------------------------
# 2. CREATE THE INPUT FORM
# ------------------------------------------------------------------------
with st.form("churn_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen?", ["No", "Yes"])
        partner = st.selectbox("Has Partner?", ["No", "Yes"])
        dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
        tenure = st.slider("Months with Company (Tenure)", 0, 72, 12)
        
    with col2:
        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=500.0)

    # Hidden defaults (we assume these for simplicity, or you can add more fields)
    submit_button = st.form_submit_button(label='Predict Churn Status')

# ------------------------------------------------------------------------
# 3. HANDLE THE PREDICTION
# ------------------------------------------------------------------------
if submit_button:
    # Prepare data payload matching the API requirements
    data = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": "Yes", # Simplified
        "MultipleLines": "No", # Simplified
        "InternetService": internet,
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": payment,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    # Show a spinner while talking to the cloud
    with st.spinner("Asking the AI model..."):
        try:
            response = requests.post(API_URL, json=data)
            
            if response.status_code == 200:
                result = response.json()
                churn_risk = result['churn_prediction']
                
                if churn_risk == "Yes":
                    st.error(f"⚠️ Prediction: **High Risk of Churn**")
                    st.write("This customer is likely to cancel.")
                else:
                    st.success(f"✅ Prediction: **Loyal Customer**")
                    st.write("This customer is likely to stay.")
            else:
                st.error("Error: Could not connect to API.")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Connection Error: {e}")