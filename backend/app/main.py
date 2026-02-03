from fastapi import FastAPI
from pydantic import BaseModel
from app.fraud_logic import predict_fraud

app = FastAPI(title="Real-Time Fraud Detection System")

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    is_international: bool
    transaction_count_24h: int

@app.post("/transaction")
def receive_transaction(transaction: Transaction):
    risk_score = predict_fraud(
        transaction.amount,
        transaction.transaction_count_24h,
        transaction.is_international
    )

    decision = "FRAUD" if risk_score > 0.5 else "SAFE"

    return {
        "transaction_id": transaction.transaction_id,
        "risk_score": round(risk_score, 2),
        "decision": decision
    }
