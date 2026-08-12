import pandas as pd
from io import StringIO

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def load_and_clean(csv_text):
    df = pd.read_csv(StringIO(csv_text))

    # Encode target
    df["Churn"] = df["Churn"].map({
        "Yes": 1,
        "No": 0
    })

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing TotalCharges
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Remove customer identifier
    df = df.drop("customerID", axis=1)

    return df


def build_pipeline(num_cols, cat_cols):

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                num_cols
            ),
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                ),
                cat_cols
            )
        ]
    )

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                LogisticRegression(
                    class_weight="balanced",
                    random_state=42,
                    max_iter=1000
                )
            )
        ]
    )

    return pipeline


if __name__ == "__main__":

    sample_csv = """customerID,tenure,MonthlyCharges,TotalCharges,Contract,InternetService,PaymentMethod,Churn
C1001,2,70.35,140.70,Month-to-month,Fiber optic,Electronic check,Yes
C1002,34,56.95,1889.50,One year,DSL,Mailed check,No
C1003,2,53.85,108.15,Month-to-month,DSL,Mailed check,Yes
C1004,45,42.30,1840.75,One year,DSL,Bank transfer (automatic),No
C1005,8,99.65,820.50,Month-to-month,Fiber optic,Electronic check,Yes
C1006,62,89.10,5681.10,Two year,Fiber optic,Credit card (automatic),No
C1007,1,20.15,20.15,Month-to-month,No,Electronic check,No
C1008,72,103.70,7382.25,Two year,Fiber optic,Bank transfer (automatic),No
C1009,5,75.30,380.15,Month-to-month,Fiber optic,Electronic check,Yes
C1010,29,60.20,1745.80,One year,DSL,Credit card (automatic),No
C1011,0,45.00, ,Month-to-month,DSL,Mailed check,No
"""

    # Step 1: Load and clean
    df = load_and_clean(sample_csv)

    print("Cleaned Dataset:")
    print(df)

    # Step 2: Define columns
    num_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    cat_cols = [
        "Contract",
        "InternetService",
        "PaymentMethod"
    ]

    print("\nNumerical Columns:")
    print(num_cols)

    print("\nCategorical Columns:")
    print(cat_cols)

    # Step 3: Separate features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Step 4: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.27,
        random_state=42,
        stratify=y
    )

    print("\nTraining Set Size:", len(X_train))
    print("Testing Set Size:", len(X_test))

    # Step 5: Build pipeline
    pipeline = build_pipeline(
        num_cols,
        cat_cols
    )

    # Step 6: Train pipeline
    pipeline.fit(
        X_train,
        y_train
    )

    # Step 7: Predict test data
    y_pred = pipeline.predict(X_test)

    print("\nTest Predictions:")
    print(y_pred)