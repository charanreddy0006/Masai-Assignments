import pandas as pd
from io import StringIO

RAW_CSV = """car_id,brand,transmission,fuel_type,km_driven,mileage,seats,price
1,Maruti,Manual,petrol,"45,000 KM",21.4 KMPL,5.0,350000
2, Honda ,Automatic,DIESEL,"30,000",19.1 KMPL,,280000
3,Maruti,Manual,Petrol,"45,000 KM",21.4 KMPL,5.0,350000
4,BMW,Automatic,diesel,"12,000 KM",14.3 KMPL,5.0,1200000
5,Ferrari,Manual,Petrol,"1,200 KM",,2.0,9999999
6, Honda ,manual,petrol,"28,000 KMS",18.9 KMPL,5.0,
7,Maruti,Manual,Petrol,"45,000 KM",21.4 KMPL,5.0,350000
8,Toyota,Automatic,Diesel,"55,000 KM",16.7 KMPL,7.0,650000
9,BMW,Automatic,Diesel,"11,000 KM",14.3 KMPL,5.0,800
10,Hyundai,Manual,CNG,"20,000 KM",24.1 KMPL,0.0,420000
"""


def clean_pipeline(raw_csv: str) -> dict:

    # -------------------------------------------------
    # Step 1: Load dataset
    # -------------------------------------------------
    df = pd.read_csv(StringIO(raw_csv))

    # -------------------------------------------------
    # Step 2: Set car_id as index
    # -------------------------------------------------
    df = df.set_index("car_id")

    # -------------------------------------------------
    # Step 3: Clean categorical columns
    # -------------------------------------------------
    text_cols = [
        "brand",
        "transmission",
        "fuel_type"
    ]

    for col in text_cols:
        df[col] = (
            df[col]
            .str.strip()
            .str.title()
        )

    # -------------------------------------------------
    # Step 4: Replace known typos
    # -------------------------------------------------
    # No explicit typo is present in the sample.
    # This step is included for the required pipeline.

    # -------------------------------------------------
    # Step 5: Convert km_driven to numeric
    # -------------------------------------------------
    df["km_driven"] = (
        df["km_driven"]
        .str.replace(",", "", regex=False)
        .str.replace("KMS", "", regex=False)
        .str.replace("KM", "", regex=False)
        .str.strip()
    )

    df["km_driven"] = pd.to_numeric(
        df["km_driven"],
        errors="coerce"
    )

    # -------------------------------------------------
    # Step 6: Convert mileage to numeric
    # -------------------------------------------------
    df["mileage"] = (
        df["mileage"]
        .str.replace("KMPL", "", regex=False)
        .str.strip()
    )

    df["mileage"] = pd.to_numeric(
        df["mileage"],
        errors="coerce"
    )

    # -------------------------------------------------
    # Step 7: First duplicate removal
    # -------------------------------------------------
    df = df.drop_duplicates()

    # -------------------------------------------------
    # Step 8: Remove rows with missing price
    # -------------------------------------------------
    df = df.dropna(
        subset=["price"]
    )

    # -------------------------------------------------
    # Step 9: Median imputation for mileage
    # -------------------------------------------------
    df["mileage"] = df["mileage"].fillna(
        df["mileage"].median()
    )

    # -------------------------------------------------
    # Step 10: Mode imputation for seats
    # -------------------------------------------------
    df["seats"] = df["seats"].fillna(
        df["seats"].mode()[0]
    )

    # -------------------------------------------------
    # Step 11: Second duplicate removal
    # -------------------------------------------------
    df = df.drop_duplicates()

    # -------------------------------------------------
    # Step 12: Remove invalid price
    # -------------------------------------------------
    df = df[df["price"] > 10000]

    # -------------------------------------------------
    # Step 13: Remove invalid seats
    # -------------------------------------------------
    df = df[df["seats"] != 0]

    # -------------------------------------------------
    # Step 14: Encode transmission
    # -------------------------------------------------
    df["transmission"] = df["transmission"].map({
        "Manual": 0,
        "Automatic": 1
    })

    # -------------------------------------------------
    # Step 15: Group rare brands
    # -------------------------------------------------
    brand_counts = df["brand"].value_counts()

    rare_brands = brand_counts[
        brand_counts < 2
    ].index

    df["brand"] = df["brand"].replace(
        rare_brands,
        "Other"
    )

    # -------------------------------------------------
    # Step 16: One-hot encode fuel_type and brand
    # -------------------------------------------------
    df = pd.get_dummies(
        df,
        columns=["fuel_type", "brand"],
        drop_first=True,
        dtype=int
    )

    # -------------------------------------------------
    # Step 17: Build summary
    # -------------------------------------------------
    result = {
        "shape": df.shape,
        "columns": list(df.columns),
        "null_count": int(
            df.isnull().sum().sum()
        ),
        "duplicates": int(
            df.duplicated().sum()
        )
    }

    return result


if __name__ == "__main__":

    result = clean_pipeline(RAW_CSV)

    print(result)