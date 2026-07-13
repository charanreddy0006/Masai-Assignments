# Entropy and Information Gain from Scratch

## 📌 Overview

This project demonstrates how to implement **Entropy** and **Information Gain** from scratch using only Python's standard library.

Instead of relying on machine learning libraries, the project manually calculates the impurity of a dataset and the reduction in impurity after splitting on a categorical feature. These concepts form the foundation of Decision Tree algorithms.

---

## 🎯 Objectives

- Implement Entropy calculation manually
- Implement Information Gain calculation manually
- Understand how Decision Trees select the best feature
- Avoid using third-party machine learning libraries

---

## 🛠 Technologies Used

- Python
- Standard Library (`math`)

---

## 📂 Dataset

The project uses a small **Play Tennis** sample dataset containing:

- Outlook
- Humidity
- PlayTennis (Target)

---

## 🔄 Workflow

```text
Dataset
    │
    ▼
Extract Target Labels
    │
    ▼
Compute Parent Entropy
    │
    ▼
Split Dataset by Feature
    │
    ▼
Compute Child Entropy
    │
    ▼
Calculate Weighted Entropy
    │
    ▼
Compute Information Gain
```

---

## 📊 Expected Output

```text
Entropy: 0.9852

Information Gain (Outlook): 0.5917
```

---

## 📚 Learning Outcomes

- Entropy
- Information Gain
- Decision Tree Fundamentals
- Feature Selection
- Probability Calculations
- Pure Python Implementation

---

## 👨‍💻 Author

**Chakri**

B.Tech Computer Science & Engineering (AI & ML)

Learning Python, Machine Learning, SQL, and Data Analytics.