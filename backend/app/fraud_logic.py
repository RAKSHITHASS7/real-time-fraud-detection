import joblib
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), "fraud_model.pkl")
model = joblib.load(model_path)

def predict_fraud(amount, transaction_count_24h, is_international):
    features = np.array([[amount, transaction_count_24h, int(is_international)]])
    probability = model.predict_proba(features)[0][1]
    return probability
