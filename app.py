from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import numpy as np
from starlette.responses import JSONResponse
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowPassword as OAuthFlowPasswordModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode as OAuthFlowAuthorizationCodeModel
from fastapi.openapi.models import OAuthFlowImplicit as OAuthFlowImplicitModel



app = FastAPI(
    title="Optasia Feature Engineering API",
    description="This API consists of 2 method requests which return the status & the results of feature engineering",
    version="1.0.0",
)

# Define your request model (modify as needed)
class FeatureEngineeringRequest(BaseModel):
    customer_id: str
    loan_date: str
    amount: float
    term: str
    fee: float
    loan_status: int
    annual_income: float

# Define your response model (modify as needed)
class FeatureEngineeringResponse(BaseModel):
    mean_loan_amount: float
    loan_count: int
    loan_status_aggregation: float
    loan_amount_std: float
    loan_amount_var: float

# API root:
@app.get("/")
async def read_root():
    return {"message": "Welcome to your FastAPI app!"}

# Check API status :
@app.get("/health/")
def check_health():
    return {"status": "UP"}

# Perform feature engineering :
@app.get("/feature_engineering/")
def perform_feature_engineering():
    # Read the input data of the customers:
    with open("cvas_data.json", "r") as file:
        data = json.load(file)

    # Check if the "data" key exists in the JSON dictionary
    if "data" in data:
        # Access the list of entries under the "data" key
        entries = data["data"]

        # Initialize lists to store calculated features
        mean_loan_amounts = []
        loan_counts = []
        loan_status_aggregations = []
        loan_amount_std = []
        loan_amount_var = []

        for entry in entries:
            loans = entry.get("loans", [])
            loan_statuses = [int(loan.get("loan_status", 0)) for loan in loans]
            loan_amounts = [float(loan.get("amount", 0.0)) for loan in loans]

            # Calculate the mean loan amount for this customer
            mean_loan_amount = np.mean(loan_amounts)
            mean_loan_amounts.append(mean_loan_amount)

            # Calculate the count of loans for this customer
            loan_count = len(loans)
            loan_counts.append(loan_count)

            # Calculate the percentage of loans that were paid back (loan_status=0)
            paid_back_percentage = (sum(loan_statuses) / loan_count) * 100
            loan_status_aggregations.append(paid_back_percentage)

            # Calculate the standard deviation and variance of loan amounts
            loan_amount_std.append(np.std(loan_amounts))
            loan_amount_var.append(np.var(loan_amounts))

        # Create a list of FeatureEngineeringResponse objects
        feature_engineering_results = [
            FeatureEngineeringResponse(
                mean_loan_amount=mean_loan_amount,
                loan_count=loan_count,
                loan_status_aggregation=loan_status_aggregation,
                loan_amount_std=loan_amount_std,
                loan_amount_var=loan_amount_var
            )
            for mean_loan_amount, loan_count, loan_status_aggregation, loan_amount_std, loan_amount_var
            in zip(mean_loan_amounts, loan_counts, loan_status_aggregations, loan_amount_std, loan_amount_var)
        ]

        return feature_engineering_results

    else:
        return {"error": "Data not found in JSON"}



if __name__ == "__main__":
    perform_feature_engineering()