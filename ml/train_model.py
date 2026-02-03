import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Starting fraud model training...")

# Load dataset
data = pd.read_csv("dataset.csv")
print("Dataset loaded")

X = data[["amount", "transaction_count_24h", "is_international"]]
y = data["is_fraud"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Model training completed")

# Save model
model_path = "fraud_model.pkl"
joblib.dump(model, model_path)

print(f"Model saved at: {os.path.abspath(model_path)}")
