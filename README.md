# Financial Wellness Scoring System & Behavioral Segmentation

## 📌 Project Overview
This project implements a **Financial Wellness Scoring System** designed to evaluate and segment users based on their financial behaviors rather than just their raw income. Unlike traditional credit risk models that predict default probability, this system uses a **behavioral scoring prototype** to compute an interpretable "Wellness Score" (0–100).

The project utilizes **Unsupervised Machine Learning (K-Means Clustering)** to discover improved customer personas and applies a **rule-based heuristic engine** to assign wellness scores.

## 📂 Repository Structure
* `Final_Code.ipynb`: The main Jupyter Notebook containing data cleaning, EDA, clustering logic, and the scoring algorithm.
* `financial_data_google_form.csv`: The dataset used for analysis, containing 200 entries of financial metrics (Income, Debt, Savings, etc.).

## 📊 Dataset Description
The dataset consists of **200 records** with the following features:
* **Income:** Annual income.
* **Monthly_Spend:** Average monthly expenditure.
* **Savings_Percent:** Percentage of income saved.
* **Emergency_Fund:** Total value of emergency funds.
* **Debt:** Total outstanding debt.
* **Savings_Amount:** Absolute value of savings.
* **Expense_to_Income_Ratio:** Ratio of expenses to income.
* **Debt_to_Income_Ratio:** Ratio of debt to income.

## 🛠️ Methodology

### 1. Data Preprocessing
* Cleaned formatting issues (e.g., removing commas from numeric strings).
* Converted data types to float for analysis.
* Standardized features using `StandardScaler` to prepare for clustering.

### 2. Customer Segmentation (K-Means Clustering)
* Used the **Elbow Method** to determine the optimal number of clusters.
* **Selected K=4** to balance cluster separation with business interpretability.
* **Identified Personas:**
    1.  **Financially Fragile:** High debt, low savings.
    2.  **High Income, Low Efficiency:** High earners who spend heavily and save little.
    3.  **Budget-Constrained but Disciplined:** Lower income but maintains healthy ratios.
    4.  **Financially Secure Savers:** High savings, low debt, strong emergency funds.

### 3. Wellness Scoring Logic (Heuristic Model)
A custom algorithm was developed to calculate a score between 0 and 100. The logic penalizes debt heavily and rewards savings behavior.

**Formula:**
$$
Score = 0.30(Savings\\%) + 0.25(1 - Exp/Inc) - 0.30(Debt/Inc) + 0.15(Emg/Inc)
$$

* **Savings Percent (30%):** Core positive indicator.
* **Debt-to-Income (30%):** Strong negative weight to reflect stability risks.
* **Expense-to-Income (25%):** Captures living within means.
* **Emergency Fund Ratio (15%):** Stabilizing factor.

### 4. Validation
* Performed correlation analysis between the generated **Wellness Score** and **Debt-to-Income Ratio**.
* Result: A strong negative correlation (**-0.94**), confirming the scoring logic correctly penalizes high-leverage users.

## 📈 Key Results
The model successfully categorized the dataset into four distinct wellness levels:
* **Low Wellness:** 121 users (Highest Risk)
* **Moderate Wellness:** 45 users
* **Good Wellness:** 18 users
* **High Wellness:** 16 users (Best Financial Health)

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/financial-wellness-scoring.git](https://github.com/yourusername/financial-wellness-scoring.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pandas numpy scikit-learn matplotlib
    ```
3.  Open the notebook:
    ```bash
    jupyter notebook Final_Code.ipynb
    ```

## 🔮 Future Improvements
* **Predictive Modeling:** Incorporate labeled data (e.g., loan defaults) to transition from a heuristic model to a supervised risk model (XGBoost/Random Forest).
* **Dashboarding:** Build a Streamlit or PowerBI dashboard to visualize individual user scores dynamically.
* **Granular Weights:** Optimize scoring weights using Principal Component Analysis (PCA) loadings.

---
*Author: [Your Name]*
*Domain: Data Science, Financial Analytics*
