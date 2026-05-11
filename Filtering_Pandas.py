import pandas as pd
import seaborn as sns

# Load Titanic dataset from seaborn
df = sns.load_dataset("titanic")

# Filter female passengers in pclass 1 or 2
filtered_df = df[
    (df["sex"] == "female") &
    (df["pclass"].isin([1, 2]))
]

# Fill missing age values with 30
filtered_df["age"] = filtered_df["age"].fillna(30)

# Sort by fare in descending order
filtered_df = filtered_df.sort_values(by="fare", ascending=False)

# Reset index
filtered_df = filtered_df.reset_index(drop=True)

# Add a new column
filtered_df["fare_group"] = "high"

# Save the result to a new CSV file
filtered_df.to_csv("female_upper_class.csv", index=False)

print("Processed file saved as female_upper_class.csv")