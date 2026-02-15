# 💰 Financial Wellness Score Calculator

A data-driven personal finance assessment tool that combines rule-based financial scoring with behavioral clustering to evaluate an individual’s financial health.

Built using Python, Scikit-learn, and Streamlit, with a pre-trained ML model deployed in an interactive web app.

## 🚀 Project Overview

This project calculates a Financial Wellness Score (0–100) based on key financial behaviors such as:

* Spending discipline
* Debt burden
* Savings quality
* Emergency fund adequacy

Alongside scoring, it uses unsupervised machine learning (K-Means clustering) to identify behavioral financial patterns for contextual insights.

**Important detail:** ML does NOT decide the score. Math does. ML only provides behavioral context.

## 🎯 Key Objectives

* Quantify financial health using transparent, explainable rules
* Segment users into behavioral finance profiles using ML
* Provide actionable insights instead of vague “save more” advice
* Deploy a pre-trained model via a user-friendly Streamlit app

## 🧠 Methodology

### 1. Rule-Based Financial Scoring (Core Logic)
The wellness score is computed using weighted components:

| Component | Weight |
| :--- | :--- |
| Expense-to-Income Ratio | 25% |
| Debt-to-Income Ratio | 30% |
| Emergency Fund Strength | 25% |
| Savings Rate Quality | 20% |

* Risk is penalized aggressively. High debt reduces the impact of good savings.
* No false optimism. Numbers don’t care about feelings.

### 2. Behavioral Clustering (Machine Learning)
* **Algorithm:** K-Means
* **Features include:** Income, Spending, Savings %, Emergency fund, Debt, Expense & debt ratios
* **Preprocessing:** StandardScaler
* **Output:** Behavioral pattern label (not a score)

**Example clusters:**
* Tight Budget Pattern
* Savings-Oriented Pattern
* High Cash Flow Pattern

This helps answer “people like you usually behave this way” without judging.

### 3. Explainability Layer
Each score includes:
* Reasons for point loss
* Clear identification of financial weaknesses
* No black-box outputs

If your score is bad, the app tells you exactly why.

## 🖥️ Streamlit Application

The Streamlit app allows users to:
1.  Enter financial details via a form (no CSV upload required)
2.  Instantly receive:
    * Wellness score
    * Risk level (Critical → Excellent)
    * Behavioral profile
    * Metric breakdown
    * Targeted improvement guidance

The ML model is pre-trained and loaded using `.pkl` files, ensuring fast and consistent predictions.

## 🛠️ Tech Stack
* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib (EDA & analysis phase)

## 📌 Future Improvements
* Add time-series tracking for returning users
* Introduce risk-adjusted investment readiness metrics
* Expand behavioral models beyond K-Means
* Deploy using Streamlit Cloud

## ⚠️ Problems / Limitations
* Uses self-reported survey data, which may contain bias or inaccuracies
* Financial scoring logic is rule-based and may not capture all real-world edge cases
* K-Means clustering assumes fixed behavioral groups and may oversimplify user behavior
* Model does not learn continuously from new user inputs
Results are indicative and not a substitute for professional financial advice


## 🚀 How to Run This Project

Clone the repository:

git clone https://github.com/shrey-408/Financial-Wellness-Scoring-Behavioral-Segmentation.git
cd Financial-Wellness-Scoring-Behavioral-Segmentation

Create a virtual environment:

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install streamlit pandas numpy scikit-learn

Run the Streamlit app:

streamlit run app.py

The app will open in your browser at:
http://localhost:8501


