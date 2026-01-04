import streamlit as st
import pandas as pd
from scoring_model import (
    calculate_wellness_score,
    get_behavioral_cluster,
    wellness_label,
    score_explanation
)

st.set_page_config(page_title="Financial Wellness Scorer", layout="wide")

st.title("🏦 Financial Wellness Score Calculator")
st.write("Assess your financial health using rule-based scoring and behavioral patterns.")

# =========================
# Input Section
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Income & Spending")
    monthly_income = st.number_input(
        "Monthly Income ($)", min_value=100.0, value=5000.0, step=100.0
    )
    monthly_spend = st.number_input(
        "Monthly Spending ($)", min_value=0.0, value=3000.0, step=100.0
    )

    st.subheader("Debt")
    total_debt = st.number_input(
        "Total Debt ($)", min_value=0.0, value=50000.0, step=1000.0
    )

with col2:
    st.subheader("Savings")
    savings_amount = st.number_input(
        "Monthly Savings ($)", min_value=0.0, value=1000.0, step=100.0
    )
    emergency_fund = st.number_input(
        "Emergency Fund ($)", min_value=0.0, value=20000.0, step=500.0
    )

# =========================
# Derived Metrics
# =========================
savings_percent = (savings_amount / monthly_income) * 100 if monthly_income > 0 else 0
expense_to_income_ratio = monthly_spend / monthly_income if monthly_income > 0 else 0

annual_income = monthly_income * 12
debt_to_income_ratio = total_debt / annual_income if annual_income > 0 else 0

months_emergency = emergency_fund / (monthly_spend + 1)

# =========================
# Scoring & Classification
# =========================
wellness_score = calculate_wellness_score(
    savings_percent,
    expense_to_income_ratio,
    debt_to_income_ratio,
    emergency_fund,
    monthly_spend
)

level = wellness_label(wellness_score)

cluster_id, cluster_name = get_behavioral_cluster(
    annual_income,
    monthly_spend,
    savings_percent,
    emergency_fund,
    total_debt,
    expense_to_income_ratio,
    debt_to_income_ratio
)

explanations = score_explanation(
    savings_percent,
    expense_to_income_ratio,
    debt_to_income_ratio,
    emergency_fund,
    monthly_spend
)

# =========================
# Results Display
# =========================
st.divider()
st.subheader("📊 Your Financial Wellness Score")

color_map = {
    "Critical": "🔴",
    "At Risk": "🟠",
    "Stable": "🟡",
    "Strong": "🟢",
    "Excellent": "🟢"
}

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Wellness Score", f"{wellness_score:.1f} / 100")
with col2:
    st.metric("Wellness Level", f"{color_map[level]} {level}")
with col3:
    st.metric("Savings Rate", f"{savings_percent:.1f}%")

# =========================
# Behavioral Profile
# =========================
st.divider()
st.subheader("👤 Behavioral Profile")
st.info(
    f"**{cluster_name}**\n\n"
    "This profile describes spending and saving patterns relative to similar users. "
    "It does not determine your wellness score."
)

# =========================
# Explainability
# =========================
st.divider()
st.subheader("📝 Why You Got This Score")

for reason in explanations:
    st.write(f"• {reason}")

# =========================
# Key Metrics (NO re-scoring)
# =========================
st.divider()
st.subheader("📈 Key Financial Metrics")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Expense / Income", f"{expense_to_income_ratio:.2f}")
with col2:
    st.metric("Debt / Income", f"{debt_to_income_ratio:.2f}")
with col3:
    st.metric("Emergency Fund (Months)", f"{months_emergency:.1f}")
with col4:
    st.metric("Annual Income", f"${annual_income:,.0f}")

# =========================
# Recommendations
# =========================
st.divider()
st.subheader("🎯 Targeted Guidance")

if level in ["Critical", "At Risk"]:
    st.write("• Focus on stabilizing cash flow and building an emergency buffer")
    st.write("• Reduce high-interest debt before increasing investments")

elif level == "Stable":
    st.write("• Increase emergency fund toward 6 months of expenses")
    st.write("• Improve savings rate while keeping debt under control")

elif level == "Strong":
    st.write("• Maintain discipline and optimize long-term investments")
    st.write("• Gradually reduce remaining debt exposure")

else:  # Excellent
    st.write("• Financial structure is resilient")
    st.write("• Focus on wealth optimization and risk diversification")
