import pandas as pd
import seaborn as sns

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Rename columns to match problem statement
df = df.rename(columns={
    "sex": "gender",
    "survived": "Survived",
    "age": "age",
    "fare": "fare",
    "pclass": "Pclass"
})

# Create summary table using groupby and single agg call
summary = df.groupby(["Pclass", "gender"]).agg(
    total_passengers=("Survived", "count"),
    survivors=("Survived", "sum"),
    survival_rate=("Survived", "mean"),
    avg_age=("age", "mean"),
    max_fare=("fare", "max")
).reset_index()

# Display summary table
print(summary)

# -----------------------------
# Written Observations
# -----------------------------

print("\nObservations:")

print("1. Female passengers in Pclass 1 had the highest survival rate,")
print("   showing that most upper-class women survived the disaster.")

print("2. Male passengers in Pclass 3 had the lowest survival rate,")
print("   indicating lower survival chances for lower-class men.")

print("3. Pclass 1 passengers paid the highest fares overall,")
print("   with maximum fares much larger than those in Pclass 2 or 3.")