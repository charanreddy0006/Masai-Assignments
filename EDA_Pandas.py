import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Create Synthetic Sales Dataset
# -----------------------------

np.random.seed(42)

categories = ["Electronics", "Clothing", "Groceries"]

data = {
    "date": pd.date_range(start="2025-01-01", periods=90),
    "category": np.random.choice(categories, 90),
    "units_sold": np.random.randint(5, 100, 90),
    "revenue": np.random.randint(500, 50000, 90),
    "discount_pct": np.random.randint(0, 40, 90)
}

df = pd.DataFrame(data)

# Add a few revenue outliers manually
df.loc[5, "revenue"] = 120000
df.loc[20, "revenue"] = 150000

# -----------------------------
# Plot 1: Histogram of units_sold
# -----------------------------

def plot_units_histogram(df):
    plt.figure(figsize=(8, 5))

    sns.histplot(df["units_sold"], bins=20)

    plt.title("Distribution of Units Sold")
    plt.xlabel("Units Sold")
    plt.ylabel("Frequency")

    plt.show()


# -----------------------------
# Plot 2: Histogram by Category
# -----------------------------

def plot_units_histogram_hue(df):
    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="units_sold",
        hue="category",
        bins=20,
        multiple="layer"
    )

    plt.title("Units Sold Distribution by Category")
    plt.xlabel("Units Sold")
    plt.ylabel("Frequency")

    plt.show()


# -----------------------------
# Plot 3: Revenue Box Plot
# -----------------------------

def plot_revenue_boxplot(df):
    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="category",
        y="revenue"
    )

    plt.title("Revenue Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")

    plt.show()


# -----------------------------
# Plot 4: Scatter Plot
# -----------------------------

def plot_scatter(df):
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="units_sold",
        y="revenue",
        hue="category"
    )

    plt.title("Units Sold vs Revenue")
    plt.xlabel("Units Sold")
    plt.ylabel("Revenue")

    plt.show()


# -----------------------------
# Compute IQR Outlier Bounds
# -----------------------------

def compute_outlier_bounds(df):

    Q1 = df["revenue"].quantile(0.25)
    Q3 = df["revenue"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print("Revenue Outlier Bounds")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")


# -----------------------------
# Main Execution
# -----------------------------

if __name__ == "__main__":

    print(df.head())

    plot_units_histogram(df)

    plot_units_histogram_hue(df)

    plot_revenue_boxplot(df)

    plot_scatter(df)

    compute_outlier_bounds(df)