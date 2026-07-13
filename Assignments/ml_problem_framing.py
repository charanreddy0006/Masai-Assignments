import pandas as pd
from io import StringIO

# Inlined sample data for the three datasets

dataset_a_csv = """transaction_id,customer_age,transaction_amount,merchant_category,hour_of_day,is_fraudulent
T001,34,12500.00,Electronics,2,1
T002,45,320.50,Grocery,14,0
T003,28,89000.00,Jewellery,3,1
T004,52,1200.00,Fuel,10,0
T005,61,450.00,Grocery,18,0
T006,29,67000.00,Electronics,1,1"""

dataset_b_csv = """company_id,founding_year,num_employees,total_funding_usd,revenue_usd,valuation_usd
C001,2015,120,5000000,2100000,18000000
C002,2018,45,1200000,450000,4500000
C003,2012,560,32000000,18000000,125000000
C004,2020,18,400000,80000,900000
C005,2016,230,9800000,5200000,42000000"""

dataset_c_csv = """user_id,sessions_per_week,avg_session_duration_min,feature_clicks,push_notif_opened
U001,12,8.5,45,22
U002,3,2.1,8,1
U003,9,6.3,31,14
U004,1,0.8,3,0
U005,7,4.2,19,9
U006,14,11.0,58,27"""

# Load datasets
df_a = pd.read_csv(StringIO(dataset_a_csv))
df_b = pd.read_csv(StringIO(dataset_b_csv))
df_c = pd.read_csv(StringIO(dataset_c_csv))


def frame_problem(df, name, identifier_cols, known_target=None, target_type=None):
    """
    Analyze dataset and return ML problem framing.
    """

    # Exclude identifier columns
    non_id_cols = [col for col in df.columns if col not in identifier_cols]

    # Step 1: Supervised vs Unsupervised
    if known_target is None:
        ml_type = "Unsupervised Clustering"
        target_info = "None / Absent"
        features = non_id_cols
        justification = (
            "No predefined outcome variable exists; the goal is to discover "
            "natural user segments or behavior patterns."
        )

    else:
        target_values = df[known_target].nunique()

        # Step 2: Regression vs Classification
        if target_type == "continuous":
            ml_type = "Supervised Regression"
            target_info = f"{known_target} (Continuous Numeric Target)"
        else:
            # Step 3: Binary vs Multi-class Classification
            if target_values == 2 or target_type == "binary":
                ml_type = "Supervised Binary Classification"
                target_info = f"{known_target} (Binary Target: 0/1)"
            else:
                ml_type = "Supervised Multi-class Classification"
                target_info = (
                    f"{known_target} (Categorical Target with {target_values} classes)"
                )

        features = [
            col for col in non_id_cols
            if col != known_target
        ]

        if ml_type == "Supervised Binary Classification":
            justification = (
                "Historical labeled examples allow prediction of a yes/no outcome."
            )
        elif ml_type == "Supervised Multi-class Classification":
            justification = (
                "Historical labeled examples allow prediction of one of several categories."
            )
        else:
            justification = (
                "Historical labeled data allows prediction of a continuous numeric value."
            )

    result = f"""
Dataset {name}
--------------------------------------------------
ML Problem Type : {ml_type}
Target Column   : {target_info}
Feature Columns : {', '.join(features)}
Business Justification : {justification}
"""
    return result


print("PROBLEM FRAMING ANALYSIS")
print("=" * 70)

# Dataset A - Fraud Detection
print(
    frame_problem(
        df_a,
        "A - Credit Card Transaction Monitoring",
        identifier_cols=["transaction_id"],
        known_target="is_fraudulent",
        target_type="binary"
    )
)

# Dataset B - Startup Valuation
print(
    frame_problem(
        df_b,
        "B - Startup Valuation Estimator",
        identifier_cols=["company_id"],
        known_target="valuation_usd",
        target_type="continuous"
    )
)

# Dataset C - User Behaviour Analysis
print(
    frame_problem(
        df_c,
        "C - Mobile App User Behaviour",
        identifier_cols=["user_id"],
        known_target=None
    )
)

print("=" * 70)