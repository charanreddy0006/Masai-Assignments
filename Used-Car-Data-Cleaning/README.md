# Used-Car Data Cleaning and Preprocessing

## 📌 Overview

This project demonstrates a complete data-cleaning and preprocessing workflow for a messy used-car dataset.

The dataset contains common real-world data-quality issues such as inconsistent text formatting, string-based numerical values, missing values, duplicate records, invalid values, and categorical variables.

The objective is to transform the raw dataset into a clean, numerical dataset that can be used for machine learning.

---

## 🎯 Objectives

The project performs the following operations:

- Load the raw used-car dataset
- Set `car_id` as the DataFrame index
- Clean categorical values using `strip()` and `title()`
- Convert string-formatted numerical columns into numeric values
- Remove duplicate records
- Handle missing values
- Remove invalid/outlier records
- Encode categorical features
- Group rare brands into `Other`
- Verify the final dataset
- Return a summary of the cleaned DataFrame

---

## 🗂️ Dataset

The sample dataset contains the following columns:

| Column | Description |
|---|---|
| `car_id` | Unique vehicle identifier |
| `brand` | Vehicle manufacturer |
| `transmission` | Manual or Automatic |
| `fuel_type` | Petrol, Diesel, CNG, etc. |
| `km_driven` | Distance driven |
| `mileage` | Vehicle mileage |
| `seats` | Number of seats |
| `price` | Vehicle price / target |

The dataset intentionally contains messy values to demonstrate a realistic preprocessing workflow.

---

## 🔄 Data Cleaning Workflow

```text
Raw Dataset
     │
     ▼
Load Dataset
     │
     ▼
Set car_id as Index
     │
     ▼
Clean Text Columns
(strip + title)
     │
     ▼
Convert String Numbers
     │
     ▼
Remove Duplicates
     │
     ▼
Handle Missing Values
     │
     ├── Missing Price → Drop Row
     ├── Missing Mileage → Median
     └── Missing Seats → Mode
     │
     ▼
Remove Duplicates Again
     │
     ▼
Remove Invalid Values
     │
     ├── price <= 10000
     └── seats == 0
     │
     ▼
Encode Categorical Features
     │
     ├── Transmission → 0 / 1
     ├── Fuel Type → One-Hot Encoding
     └── Rare Brands → Other
     │
     ▼
Clean Numerical Dataset