import streamlit as st
import requests
import json
from predict import predict_churn, columns


st.set_page_config(page_title="Churn Predictor", page_icon="📞", layout="centered")

# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

churn_lottie = load_lottie_url("https://lottie.host/8bc5b12d-c4fa-4e57-bd59-33d104352dfc/GcFtLhEKMC.json")

# Title with animation
st.markdown("<h1 style='text-align:center;'>📞 Customer Churn Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Enter customer details to predict churn</h4>", unsafe_allow_html=True)
st.markdown("---")

with st.container():
    col1, col2 = st.columns([2, 1])
    with col2:
        if churn_lottie:
            st_lottie = st.components.v1.html(f"""
            <body style="margin:0">
            <lottie-player src="https://lottie.host/8bc5b12d-c4fa-4e57-bd59-33d104352dfc/GcFtLhEKMC.json" 
            background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            </body>
            """, height=300)
    with col1:
        st.subheader("🔍 Customer Info")

        gender = st.selectbox("Gender", ["Female", "Male"])
        senior = st.selectbox("Senior Citizen", ["No", "Yes"])
        partner = st.selectbox("Has Partner?", ["No", "Yes"])
        dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
        tenure = st.slider("Tenure (Months)", 0, 72, 12)
        monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
        total_charges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", [
            "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
        ])

if st.button("🎯 Predict"):
    user_input = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        f"InternetService_{internet_service}": 1,
        f"Contract_{contract}": 1,
        f"PaymentMethod_{payment_method}": 1
    }

    for col in columns:
        if col not in user_input:
            user_input[col] = 0

    prediction, probability = predict_churn(user_input)

    st.success(f"🎯 Prediction: **{'Churn' if prediction else 'Not Churn'}**")
    st.info(f"📊 Probability of churn: **{probability * 100:.2f}%**")
