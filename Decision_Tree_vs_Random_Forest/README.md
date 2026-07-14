# Decision Tree vs Random Forest - Feature Importance Comparison

## 📌 Overview

This project compares how a **Decision Tree Classifier** and a **Random Forest Classifier** assign feature importance using a passenger survival dataset.

Both models are trained on the same preprocessed data, and their feature importance values are compared to understand how each algorithm selects important features.

---

## 🎯 Objectives

- Load the passenger survival dataset
- Apply Label Encoding
- Apply One-Hot Encoding
- Train a Decision Tree model
- Train a Random Forest model
- Compare feature importance values

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 📂 Dataset

The dataset contains:

- survived (Target)
- age
- sibsp
- pclass
- fare
- embarked
- sex

---

## 🔄 Workflow

```text
Passenger Dataset
        │
        ▼
Load Dataset
        │
        ▼
Label Encoding
        │
        ▼
One-Hot Encoding
        │
        ▼
Feature Selection
        │
        ▼
Train Decision Tree
        │
        ▼
Train Random Forest
        │
        ▼
Extract Feature Importance
        │
        ▼
Compare Results
```

---

## 🌳 Decision Tree

- Builds a single decision tree.
- Often relies on one dominant feature.
- Simpler and easier to interpret.

---

## 🌲 Random Forest

- Builds multiple decision trees.
- Combines their predictions.
- Distributes importance across multiple useful features.
- Reduces overfitting and improves generalization.

---

## 📊 Expected Output

The program returns a dictionary containing feature importance values for:

- Decision Tree
- Random Forest

The comparison shows that the Decision Tree assigns most importance to one feature, while the Random Forest distributes importance more evenly across several features.

---

## 📚 Learning Outcomes

- Decision Tree Classification
- Random Forest Classification
- Feature Importance
- Label Encoding
- One-Hot Encoding
- Ensemble Learning
- Model Comparison

---

## 👨‍💻 Author

**Chakri**

B.Tech Computer Science & Engineering (AI & ML)

Learning Python, Machine Learning, SQL, and Data Analytics.