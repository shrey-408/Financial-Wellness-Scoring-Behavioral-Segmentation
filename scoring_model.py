import joblib
import numpy as np

# ==============================
# Load pre-trained ML components
# ==============================
scaler = joblib.load("scaler.pkl")
kmeans = joblib.load("kmeans.pkl")

# Behavioral clusters (descriptive, not judgmental)
cluster_map = {
    0: "Tight Budget Pattern",
    1: "Savings-Oriented Pattern",
    2: "High Cash Flow Pattern"
}

# ==============================
# 1. Financial Wellness Scoring
# ==============================
def calculate_wellness_score(
    savings_percent,
    expense_to_income_ratio,
    debt_to_income_ratio,
    emergency_fund,
    monthly_spend
):
    """
    Rule-based financial wellness score (0–100).
    Designed to penalize risk, not flatter users.
    """

    score = 0

    # ---- Expense Discipline (25%) ----
    er = expense_to_income_ratio
    if er <= 0.4:
        expense_score = 25
    elif er >= 1.0:
        expense_score = 0
    else:
        expense_score = (1 - ((er - 0.4) / 0.6)) * 25

    # ---- Debt Burden (30%) ----
    dr = debt_to_income_ratio
    if dr <= 0.5:
        debt_score = 30
    elif dr >= 3.0:
        debt_score = 0
    else:
        debt_score = (1 - ((dr - 0.5) / 2.5)) * 30

    # ---- Emergency Fund Strength (25%) ----
    months_cover = emergency_fund / (monthly_spend + 1)
    if months_cover >= 6:
        emergency_score = 25
    else:
        emergency_score = (months_cover / 6) * 25

    # ---- Savings Quality (20%) ----
    savings_score = min(savings_percent / 25, 1.0) * 20

    # Penalize savings if debt is high
    if dr > 1:
        savings_score *= 0.6
    if dr > 2:
        savings_score *= 0.4

    score = expense_score + debt_score + emergency_score + savings_score
    return round(score, 2)

# ==============================
# 2. Behavioral Clustering (ML)
# ==============================
def get_behavioral_cluster(
    income,
    monthly_spend,
    savings_percent,
    emergency_fund,
    debt,
    expense_to_income_ratio,
    debt_to_income_ratio
):
    """
    Returns behavioral cluster for context only.
    ML does NOT determine wellness score.
    """

    savings_amount = savings_percent * income / 100

    user_data = np.array([[
        income,
        monthly_spend,
        savings_percent,
        emergency_fund,
        debt,
        savings_amount,
        expense_to_income_ratio,
        debt_to_income_ratio
    ]])

    user_scaled = scaler.transform(user_data)
    cluster_id = int(kmeans.predict(user_scaled)[0])
    cluster_name = cluster_map.get(cluster_id, "Unknown Pattern")

    return cluster_id, cluster_name

# ==============================
# 3. Wellness Level Mapping
# ==============================
def wellness_label(score):
    """
    Risk-based interpretation of score.
    """
    if score < 35:
        return "Critical"
    elif score < 55:
        return "At Risk"
    elif score < 70:
        return "Stable"
    elif score < 85:
        return "Strong"
    else:
        return "Excellent"

# ==============================
# 4. Explainability Layer
# ==============================
def score_explanation(
    savings_percent,
    expense_to_income_ratio,
    debt_to_income_ratio,
    emergency_fund,
    monthly_spend
):
    """
    Explains WHY points were lost.
    Aligned exactly with scoring logic.
    """

    reasons = []
    months_cover = emergency_fund / (monthly_spend + 1)

    # Spending behavior
    if expense_to_income_ratio > 0.7:
        reasons.append("Spending consumes most of income")
    elif expense_to_income_ratio > 0.5:
        reasons.append("Spending limits long-term growth")

    # Savings behavior
    if savings_percent < 10:
        reasons.append("Savings rate is too low")
    elif savings_percent < 20:
        reasons.append("Savings rate could be stronger")

    # Debt burden
    if debt_to_income_ratio > 2:
        reasons.append("Debt level is dangerously high")
    elif debt_to_income_ratio > 1:
        reasons.append("Debt increases financial risk")

    # Emergency preparedness
    if months_cover < 1:
        reasons.append("Emergency fund is critically insufficient")
    elif months_cover < 3:
        reasons.append("Emergency fund is below safety threshold")

    if not reasons:
        reasons.append("Financial behavior is balanced and resilient")

    return reasons
