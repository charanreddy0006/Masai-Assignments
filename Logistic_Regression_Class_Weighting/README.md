# Logistic Regression with Class Weighting for Fraud Detection

## 📌 Project Overview

Class imbalance is one of the biggest challenges in fraud detection systems. In real-world financial datasets, fraudulent transactions usually represent only a very small percentage of all transactions, causing machine learning models to become biased toward the majority (legitimate) class.

This project demonstrates how **Logistic Regression** performs on an imbalanced transaction dataset and compares the performance of:

- **Baseline Logistic Regression**
- **Balanced Logistic Regression** using `class_weight="balanced"`

The project also manually computes class weights using the standard class weight formula before training the models.

---

## 🎯 Objectives

The objectives of this project are to:

- Build a transaction dataset using Pandas.
- Manually compute class weights using the standard class-weight formula.
- Split the dataset while preserving the original class distribution.
- Scale numerical features using `StandardScaler`.
- Train a baseline Logistic Regression classifier.
- Train a balanced Logistic Regression classifier.
- Compare the performance of both models using common evaluation metrics.

---

## 🗂 Dataset Description

The dataset represents a small collection of financial transactions.

| Feature | Description |
|----------|-------------|
| **V1** | PCA-transformed transaction feature |
| **V2** | PCA-transformed transaction feature |
| **Amount** | Transaction amount |
| **Class** | Target variable (0 = Legitimate, 1 = Fraud) |

### Class Distribution

| Class | Meaning | Records |
|--------|---------|---------|
| 0 | Legitimate Transaction | 9 |
| 1 | Fraudulent Transaction | 3 |

This dataset is intentionally imbalanced to demonstrate the effect of class weighting.

---

# 📐 Manual Class Weight Calculation

Class weights are calculated using the formula:

\[
\text{Class Weight} =
\frac{\text{Total Samples}}
{\text{Number of Classes} \times \text{Samples in that Class}}
\]

### For this dataset

Total Samples = **12**

Number of Classes = **2**

Legitimate Transactions = **9**

Fraudulent Transactions = **3**

### Computed Weights

| Class | Weight |
|---------|--------|
| Legitimate (0) | **0.667** |
| Fraud (1) | **2.000** |

The minority class receives a larger weight, encouraging the model to pay more attention to fraud cases.

---

# 🛠 Technologies Used

- Python 3
- Pandas
- Scikit-learn

Libraries Used

- pandas
- train_test_split
- StandardScaler
- LogisticRegression
- accuracy_score
- precision_score
- recall_score
- f1_score

---

# ⚙ Data Preprocessing

The following preprocessing steps are performed before model training:

- Create a DataFrame from the dataset.
- Separate features and target variable.
- Perform stratified train-test split.
- Fit `StandardScaler` only on the training data.
- Transform both training and testing datasets using the same scaler.

---

# 🤖 Machine Learning Models

## 1️⃣ Baseline Logistic Regression

Parameters:

```python
LogisticRegression(
    random_state=42,
    max_iter=1000
)
```

Characteristics

- No class weighting
- Learns directly from the original data distribution

---

## 2️⃣ Balanced Logistic Regression

Parameters

```python
LogisticRegression(
    class_weight="balanced",
    random_state=42,
    max_iter=1000
)
```

Characteristics

- Automatically applies higher weight to the minority class
- Helps reduce bias toward the majority class
- Frequently improves Recall for fraud detection problems

---

# 📊 Model Evaluation Metrics

The models are evaluated using the following classification metrics.

| Metric | Description |
|---------|-------------|
| Accuracy | Overall prediction accuracy |
| Precision | Percentage of predicted frauds that are actually fraud |
| Recall | Percentage of actual frauds correctly detected |
| F1 Score | Harmonic mean of Precision and Recall |

---

# 📈 Expected Output

### Manual Class Weights

```text
Class 0 Weight : 0.667
Class 1 Weight : 2.000
```

### Dataset Split

```text
Training Records : 9

Testing Records : 3

Training Distribution

Class 0 : 7

Class 1 : 2

Testing Distribution

Class 0 : 2

Class 1 : 1
```

### Baseline Logistic Regression

```text
Accuracy : 1.0
Precision : 1.0
Recall : 1.0
F1 Score : 1.0
```

### Balanced Logistic Regression

```text
Accuracy : 1.0
Precision : 1.0
Recall : 1.0
F1 Score : 1.0
```

---

# 📌 Project Workflow

```text
                    Start
                      │
                      ▼
          Create Transaction Dataset
                      │
                      ▼
        Compute Class Weights Manually
                      │
                      ▼
      Split Dataset (Stratified Sampling)
                      │
                      ▼
          Standardize Numerical Features
                      │
                      ▼
        Train Baseline Logistic Regression
                      │
                      ▼
        Train Balanced Logistic Regression
                      │
                      ▼
          Evaluate Both Models
                      │
                      ▼
         Compare Classification Metrics
                      │
                      ▼
                   End
```

---

# 📁 Project Structure

```text
Logistic-Regression-Class-Weighting/
│
├── Logistic_Regression_Class_Weighting.ipynb
├── logistic_regression_class_weighting.py
├── README.md
└── requirements.txt
```

---

# 🎓 Key Learning Outcomes

After completing this project, you will understand:

- Binary Classification
- Imbalanced Dataset Handling
- Manual Class Weight Calculation
- Stratified Sampling
- Feature Scaling
- Logistic Regression
- Balanced Logistic Regression
- Model Evaluation
- Precision vs Recall
- Importance of F1 Score in Fraud Detection

---

# 🚀 Future Improvements

Some possible enhancements include:

- Larger transaction dataset
- Cross-validation
- Hyperparameter tuning using GridSearchCV
- ROC Curve Analysis
- Precision-Recall Curve
- Threshold optimization
- SMOTE oversampling
- Ensemble learning methods

---


## ⭐ If you found this project helpful, consider giving it a star on GitHub!