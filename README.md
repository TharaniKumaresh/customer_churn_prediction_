# 📞 Customer Churn Prediction – ML Project

This project uses machine learning to predict whether a telecom customer will **churn (leave)** based on various features like contract type, internet service, tenure, and monthly charges.

---

## 🚀 Features

- ✅ Trained ML model with 78%+ accuracy
- 🎯 Churn prediction with probability
- 📊 Streamlit UI for user interaction
- 🧠 Preprocessing + One-Hot Encoding
- 💼 Built on Telco Customer Churn dataset

---

## 📂 Project Structure

customer_churn_prediction/
├── app.py # Streamlit UI
├── src/
│ ├── preprocess.py # Data loading and encoding
│ ├── model.py # Training + saving model
│ └── predict.py # Prediction logic
├── model/
│ ├── churn_model.pkl # Trained ML model
│ └── columns.pkl # Saved feature columns
├── data/
│ └── Telco-Customer-Churn.csv
├── .streamlit/
│ └── config.toml # Theme config
└── README.md

---

## 🧪 Dataset

- **Source:** [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Size:** ~7,000+ records
- **Features:** Contract, Internet Service, Charges, Tenure, etc.

---

## 🛠️ How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/customer_churn_prediction.git
   cd customer_churn_prediction

# install requirements
pip install -r requirements.txt

# train the model(optional)
python -m src.model

# Launch Streamlit UI
streamlit run app.py

🧠 Tech Stack
Python
Pandas / NumPy
Scikit-learn
Streamlit
Lottie Animations


