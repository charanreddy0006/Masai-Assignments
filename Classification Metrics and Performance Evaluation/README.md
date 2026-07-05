# ROC Curve and Threshold Analysis using Logistic Regression

## Overview

This project builds a complete fraud detection evaluation pipeline using Logistic Regression.

Instead of directly predicting classes, the model predicts fraud probabilities.

Different decision thresholds are evaluated to determine the best balance between Precision and Recall.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## Workflow

```text
Transaction Dataset
        │
        ▼
Load Dataset
        │
        ▼
Train-Test Split
        │
        ▼
Feature Scaling
        │
        ▼
Train Logistic Regression
        │
        ▼
Predict Fraud Probability
        │
        ▼
ROC Curve
        │
        ▼
AUC Score
        │
        ▼
Threshold Analysis
        │
        ▼
Threshold Recommendation
```

---

## Features

- Logistic Regression
- Feature Scaling
- Probability Prediction
- ROC Curve
- AUC Score
- Precision
- Recall
- F1 Score
- Threshold Optimization

---

## Learning Outcomes

- Binary Classification
- Probability Prediction
- ROC Curve Analysis
- AUC Interpretation
- Threshold Selection
- Precision–Recall Tradeoff
- Fraud Detection

---

## Final Recommendation

The recommended threshold is **0.1** because it provides the highest Recall, minimizing missed fraud cases and aligning with the company's fraud detection policy.

---

