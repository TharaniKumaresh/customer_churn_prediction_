import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna()  # Drop missing values

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna(subset=['TotalCharges'])

    # Drop customerID
    df = df.drop('customerID', axis=1)

    return df

def encode_data(df):
    # Binary encoding
    binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    # Encode gender
    df['gender'] = df['gender'].map({'Female': 1, 'Male': 0})

    # One-hot encode other categorical columns
    df = pd.get_dummies(df, drop_first=True)

    return df
