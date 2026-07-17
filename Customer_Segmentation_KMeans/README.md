# Customer Segmentation using K-Means Clustering

## 📌 Project Overview

Customer segmentation helps businesses group customers with similar characteristics, enabling personalized marketing strategies and better business decisions.

This project applies the **K-Means Clustering** algorithm to segment customers based on **Annual Income** and **Spending Score**. Before clustering, the numerical features are standardized using **StandardScaler** to ensure equal contribution to distance calculations. The optimal number of clusters is selected by comparing **Silhouette Scores** for multiple values of **K**, and the final clusters are analyzed through their average income and spending behavior.

---

## 🎯 Objectives

- Load customer data into a Pandas DataFrame.
- Select Annual Income and Spending Score as clustering features.
- Standardize features using `StandardScaler`.
- Evaluate multiple K values using Silhouette Score.
- Identify the optimal number of clusters.
- Train the final K-Means clustering model.
- Assign cluster labels to each customer.
- Generate a cluster profile using mean Annual Income and Spending Score.

---

## 🗂 Dataset Description

| Feature | Description |
|---------|-------------|
| CustomerID | Unique customer identifier |
| AnnualIncome | Customer's annual income |
| SpendingScore | Spending score assigned based on purchasing behavior |

The dataset contains **10 customer records**.

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn

### Libraries

- pandas
- StandardScaler
- KMeans
- silhouette_score

---

## ⚙ Workflow

```text
Customer Dataset
        │
        ▼
Select Features
        │
        ▼
Standardize Features
        │
        ▼
Evaluate K = 2, 3, 4
        │
        ▼
Compute Silhouette Score
        │
        ▼
Select Best K
        │
        ▼
Train Final K-Means Model
        │
        ▼
Assign Cluster Labels
        │
        ▼
Generate Cluster Profiles
```

---

## 📊 Model Evaluation

The Silhouette Score is calculated for:

- K = 2
- K = 3
- K = 4

The value of **K** with the highest Silhouette Score is selected as the optimal number of clusters.

---

## 📈 Expected Results

- Feature scaling improves clustering performance.
- Silhouette Score identifies the optimal cluster count.
- Each customer is assigned to a cluster.
- Mean Annual Income and Spending Score are calculated for every cluster.

---

## 📁 Project Structure

```text
Customer-Segmentation-KMeans/
│
├── Customer_Segmentation_KMeans.ipynb
├── customer_segmentation_kmeans.py
├── README.md
└── requirements.txt
```

---

## 🎓 Learning Outcomes

- Unsupervised Learning
- Customer Segmentation
- K-Means Clustering
- Feature Scaling
- StandardScaler
- Silhouette Score
- Cluster Profiling
- Data Analysis

---

## 🚀 Future Improvements

- Visualize clusters using Matplotlib or Seaborn.
- Apply the Elbow Method alongside Silhouette Score.
- Experiment with MiniBatchKMeans for large datasets.
- Use additional customer attributes for richer segmentation.
- Compare clustering results with DBSCAN and Hierarchical Clustering.

---

## 👨‍💻 Author

**M. Charan Kumar Reddy**

**B.Tech – Computer Science & Engineering (Artificial Intelligence & Machine Learning)**

Passionate about **Machine Learning, Data Science, Python, SQL, Cloud Computing, and Software Development.**