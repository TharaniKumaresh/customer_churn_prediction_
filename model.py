import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from src.preprocess import load_data, encode_data

def train_model():
    # Load & preprocess data
    df = load_data("data/churn_data.csv")
    df = encode_data(df)

    # Split features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {acc*100:.2f}%")
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

    # Save model and columns
    joblib.dump(clf, "src/model.pkl")
    joblib.dump(X.columns.tolist(), "src/columns.pkl")
    print("🎉 Model and columns saved!")

if __name__ == "__main__":
    train_model()
