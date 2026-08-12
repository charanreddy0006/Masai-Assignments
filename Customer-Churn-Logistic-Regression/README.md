# Customer Churn Prediction using Logistic Regression

## 📌 Project Overview

This project demonstrates an end-to-end **customer churn prediction pipeline** using Logistic Regression.

The project focuses on correctly handling a dataset containing both numerical and categorical customer attributes. Instead of preprocessing every feature manually, the project uses Scikit-learn's `ColumnTransformer` and `Pipeline` to create a structured and reusable machine learning workflow.

The model predicts whether a customer is likely to churn based on customer tenure, charges, contract type, internet service, and payment method.

---

## 🎯 Objectives

The main objectives of this project are:

- Load and clean customer data.
- Convert the churn target into numerical values.
- Handle invalid and missing `TotalCharges` values.
- Remove the customer identifier.
- Separate numerical and categorical features.
- Scale numerical features.
- One-hot encode categorical features.
- Build a preprocessing pipeline.
- Train a balanced Logistic Regression model.
- Generate predictions for unseen test data.

---

## 🗂 Dataset Description

The sample dataset contains customer records with the following attributes:

| Column | Type | Description |
|---|---|---|
| `customerID` | Identifier | Unique customer identifier |
| `tenure` | Numerical | Number of months the customer has stayed |
| `MonthlyCharges` | Numerical | Customer's monthly service charge |
| `TotalCharges` | Numerical | Total amount charged to the customer |
| `Contract` | Categorical | Customer contract type |
| `InternetService` | Categorical | Type of internet service |
| `PaymentMethod` | Categorical | Customer payment method |
| `Churn` | Target | Whether the customer left the service |

### Target Encoding

The `Churn` column is converted as follows:

```text
Yes → 1
No  → 0