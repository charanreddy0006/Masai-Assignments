# Ridge Regression Cross-Validation Analysis

## Overview

This project demonstrates how to analyze the results of **5-Fold Cross Validation** performed on a Ridge Regression model for predicting used car prices.

The objective is to identify the best regularization parameter (**Alpha**) by comparing model performance using **Mean R²** and **Mean Absolute Error (MAE)**. The project also explains how different alpha values affect the model and recommends the appropriate evaluation metric for business use.

---

## Objectives

- Load cross-validation results into a Pandas DataFrame.
- Identify the optimal alpha value.
- Analyze how alpha affects Ridge Regression.
- Recommend the final model training strategy.
- Select the most appropriate regression error metric.
- Compare Ridge Regression with Lasso Regression.

---

## Technologies Used

- Python
- Pandas

---

## Dataset

The project uses the provided **5-fold cross-validation results** containing:

- Alpha
- Mean R²
- Mean MAE

---

## Workflow

```text
Cross Validation Results
            │
            ▼
Load into Pandas DataFrame
            │
            ▼
Find Best Alpha
            │
            ▼
Analyze Model Performance
            │
            ▼
Recommend Training Strategy
            │
            ▼
Choose Best Error Metric
            │
            ▼
Compare Ridge vs Lasso
```

---

## Project Steps

### Step 1: Load Cross-Validation Results

- Create a Pandas DataFrame.
- Store Alpha, Mean R² and Mean MAE.

---

### Step 2: Identify Optimal Alpha

The best alpha is selected using:

- Highest Mean R²
- Lowest acceptable Mean MAE

Result:

- **Best Alpha = 1**
- **Mean R² = 0.682**
- **Mean MAE = 219400**

---

### Step 3: Alpha Behavior Analysis

The project explains how increasing alpha changes the Ridge Regression model.

Observations:

- Small alpha values produce better model performance.
- Alpha = 1 provides the best balance.
- Large alpha values increase regularization.
- Excessively large alpha values lead to underfitting.

---

### Step 4: Model Training Strategy

Recommended workflow:

1. Select the optimal alpha.
2. Retrain the Ridge Regression model using the complete training dataset.
3. Evaluate the final model on the unseen test dataset.

---

### Step 5: Error Metric Recommendation

When minimizing large vehicle price prediction errors is important:

- RMSE is preferred over MAE.
- RMSE penalizes larger prediction errors more heavily.

---

### Step 6: Ridge vs Lasso

| Ridge Regression | Lasso Regression |
|-----------------|------------------|
| Uses L2 Regularization | Uses L1 Regularization |
| Shrinks coefficients | Shrinks coefficients |
| Does not remove features | Can remove features by making coefficients zero |

---

## Expected Output

The program prints:

- Best Alpha
- Mean R²
- Mean MAE
- Alpha behavior analysis
- Recommended training strategy
- Recommended evaluation metric
- Ridge vs Lasso comparison

---

## Learning Outcomes

After completing this project, you will understand:

- Ridge Regression
- Cross Validation
- Hyperparameter Tuning
- Regularization
- Model Evaluation
- Regression Metrics
- Feature Shrinkage
- Difference between Ridge and Lasso Regression

---

## Conclusion

The analysis concludes that **Alpha = 1** provides the best balance between prediction accuracy and model generalization. Very large alpha values reduce model performance due to excessive regularization. For businesses where large prediction errors are costly, **RMSE** is the preferred evaluation metric.