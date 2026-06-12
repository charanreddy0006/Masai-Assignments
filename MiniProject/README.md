# 🎓 AI Learning Lab – Data Analysis Project

## 📌 Project Overview

The **AI Learning Lab Data Analysis Project** is a complete end-to-end data analytics workflow designed to analyze student learning behavior, performance, attendance, and engagement in an AI learning program.

The project demonstrates how raw educational data can be transformed into meaningful insights through:

* Data Loading
* Data Exploration
* Data Cleaning
* Data Analysis
* Data Visualization
* Report Generation
* Database Querying using SQLite

This project simulates a real-world data analytics pipeline used by educational institutions and learning platforms to monitor student progress and identify students who may need additional support.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Explore and understand a dataset using Pandas.
* Clean inconsistent and missing data.
* Create new analytical features.
* Analyze student performance.
* Generate visual reports using Matplotlib.
* Export summaries into JSON format.
* Store and query data using SQLite.
* Practice a complete data analytics workflow.

---

# 📂 Project Structure

```text
AI-Learning-Lab/
│
├── ai_learning_lab.csv
│
├── task1_load_explore.py
├── task2_clean_data.py
├── task3_analyze_data.py
├── task4_visual_report.py
├── bonus_sql_analysis.py
│
├── cleaned_ai_learning_lab.csv
├── learning_lab.db
├── learning_summary.json
│
├── topic_score_chart.png
├── performance_level_chart.png
├── attendance_chart.png
├── study_hours_chart.png
│
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming Language          |
| Pandas     | Data Loading and Analysis     |
| NumPy      | Numerical Operations          |
| Matplotlib | Data Visualization            |
| SQLite     | Database Storage and Querying |
| JSON       | Report Export                 |

---

# 📊 Dataset Description

The dataset contains information about students participating in AI learning activities.

## Important Columns

| Column           | Description             |
| ---------------- | ----------------------- |
| student_name     | Student Name            |
| topic            | Learning Topic          |
| attendance       | Attendance Status       |
| assignment_score | Assignment Marks        |
| quiz_score       | Quiz Marks              |
| study_hours      | Study Time              |
| feedback_rating  | Student Feedback Rating |
| tool_used        | Learning Tool Used      |
| batch            | Student Batch           |
| lab_completed    | Lab Completion Status   |
| api_used         | API Usage Status        |

---

# 🚀 Task 1 – Load and Explore the Dataset

## Objective

Understand the dataset structure before performing any analysis.

## Operations Performed

* Imported Pandas.
* Loaded the CSV file.
* Displayed dataset shape.
* Displayed first five rows.
* Displayed column names.
* Displayed data types.
* Checked missing values.
* Checked duplicate rows.
* Generated value counts for:

  * Topic
  * Attendance

## Concepts Learned

* DataFrames
* CSV Loading
* Dataset Inspection
* Missing Value Detection
* Frequency Analysis

---

# 🧹 Task 2 – Data Cleaning and Preparation

## Objective

Prepare the dataset for accurate analysis.

## Cleaning Steps

### Duplicate Removal

Removed repeated records using:

```python
drop_duplicates()
```

### Space Removal

Applied:

```python
str.strip()
```

to:

* student_name
* topic
* tool_used

### Text Standardization

Converted values into title case:

```python
str.title()
```

Columns:

* attendance
* lab_completed
* api_used

### Invalid Value Handling

#### assignment_score

Invalid if:

```text
score < 0
score > 100
```

#### quiz_score

Invalid if:

```text
score < 0
score > 100
```

#### study_hours

Invalid if:

```text
negative value
```

#### feedback_rating

Valid range:

```text
1 to 5
```

### Missing Value Treatment

| Column           | Strategy |
| ---------------- | -------- |
| assignment_score | Mean     |
| quiz_score       | Mean     |
| study_hours      | Median   |
| feedback_rating  | Median   |

## Output

```text
cleaned_ai_learning_lab.csv
```

---

# 📈 Task 3 – Learning Data Analysis

## Objective

Generate performance insights from cleaned data.

## New Feature Created

### Total Score

Formula:

```text
total_score =
assignment_score + quiz_score
```

### Performance Levels

| Total Score | Category      |
| ----------- | ------------- |
| 160+        | Excellent     |
| 120–159     | Good          |
| 80–119      | Average       |
| Below 80    | Needs Support |

## Analysis Performed

### Average Assignment Score

Calculated using:

```python
mean()
```

### Average Quiz Score

Calculated using:

```python
mean()
```

### Average Study Hours

Calculated using:

```python
mean()
```

### Performance Distribution

Calculated using:

```python
value_counts()
```

### Topic-wise Analysis

Calculated using:

```python
groupby()
```

### Batch-wise Analysis

Calculated using:

```python
groupby()
```

### Needs Support Identification

Students identified if:

```text
performance_level = Needs Support
```

---

# 📊 Task 4 – Data Visualization

## Objective

Present insights visually.

### Chart 1

#### Average Total Score by Topic

Type:

```text
Bar Chart
```

Output:

```text
topic_score_chart.png
```

---

### Chart 2

#### Student Count by Performance Level

Type:

```text
Bar Chart
```

Output:

```text
performance_level_chart.png
```

---

### Chart 3

#### Attendance Distribution

Type:

```text
Pie Chart
```

Output:

```text
attendance_chart.png
```

---

### Chart 4

#### Average Study Hours by Topic

Type:

```text
Line Chart
```

Output:

```text
study_hours_chart.png
```

---

# 📄 JSON Summary Report

The project automatically generates:

```text
learning_summary.json
```

The report contains:

```json
{
  "total_students": 100,
  "average_assignment_score": 78.5,
  "average_quiz_score": 74.2,
  "average_study_hours": 6.3,
  "most_common_topic": "Python"
}
```

---

# 🗄 Bonus Task – SQLite Database Analysis

## Objective

Store and analyze data using SQL.

## Database Created

```text
learning_lab.db
```

## Table Created

```text
student_learning
```

## Query 1

Average Assignment Score by Topic

```sql
SELECT topic,
AVG(assignment_score)
FROM student_learning
GROUP BY topic;
```

---

## Query 2

Student Count by Batch

```sql
SELECT batch,
COUNT(*)
FROM student_learning
GROUP BY batch;
```

---

## Query 3

Students with Total Score Below 80

```sql
SELECT student_name,
total_score
FROM student_learning
WHERE total_score < 80;
```

---

# 📚 Skills Demonstrated

This project demonstrates:

* Data Loading
* Data Cleaning
* Data Transformation
* Feature Engineering
* Data Aggregation
* Exploratory Data Analysis
* Visualization
* Report Generation
* JSON Handling
* SQL Querying
* SQLite Database Management

---

# 🎓 Learning Outcomes

After completing this project, you will understand:

* How real-world datasets are cleaned.
* How missing values are handled.
* How data is analyzed using Pandas.
* How charts are created using Matplotlib.
* How reports are exported.
* How SQL is used alongside Python.
* How a complete data analytics workflow operates.

---

# 🔮 Future Improvements

Possible enhancements include:

* Interactive dashboards using Streamlit.
* Advanced visualizations using Seaborn.
* Machine Learning-based performance prediction.
* Student recommendation system.
* Automated PDF report generation.
* Real-time analytics dashboard.

---

# 👨‍💻 Author

Chakri

B.Tech Student | Data Analytics & Python Enthusiast

This project was developed as part of a hands-on learning exercise to practice Data Analysis, Visualization, and Database Management using Python.
