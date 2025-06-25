import joblib
import pandas as pd

# Load trained model and columns
try:
    model = joblib.load("src/model.pkl")
    columns = joblib.load("src/columns.pkl")
except Exception as e:
    print("❌ Failed to load model or columns:", e)
    model = None
    columns = []

def predict_churn(user_input_dict):
    """
    Takes a dictionary of user input, prepares the DataFrame,
    and returns prediction + probability.
    """
    try:
        print("✅ Running prediction...")

        # Convert dict to single-row DataFrame
        input_df = pd.DataFrame([user_input_dict])

        # Fill missing one-hot encoded columns with 0
        for col in columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Ensure column order matches training
        input_df = input_df[columns]

        # Predict
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]  # probability of class '1'

        return prediction, prob

    except Exception as e:
        print("❌ Error during prediction:", e)
        return None


# ✅ Standalone test block
if __name__ == "__main__":
    print("👋 Predict script started")

    sample_input = {
        "gender": 1,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 0,
        "tenure": 12,
        "MonthlyCharges": 75.0,
        "TotalCharges": 800.0,
        "InternetService_Fiber optic": 1,
        "Contract_Two year": 0,
        "PaymentMethod_Electronic check": 1
        # Add any more one-hot fields if needed (set as 0/1)
    }

    result, probability = predict_churn(sample_input)
    if result is not None:
        print(f"🎯 Prediction: {'Churn' if result else 'Not Churn'} ({probability*100:.2f}%)")
