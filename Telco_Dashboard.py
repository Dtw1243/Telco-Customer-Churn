import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Telco Customer Churn Dashboard")

# =========================
# LOAD DATA
# =========================
data = pd.read_csv("Telco Customer Retention CSV.csv")

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filters")

contract_type = st.sidebar.selectbox(
    "Contract Type",
    data["Contract"].unique()
)

filtered_df = data[data["Contract"] == contract_type]

# =========================
# OVERVIEW
# =========================
st.subheader("Customer Overview")

st.dataframe(filtered_df.head())

st.write("Rows:", filtered_df.shape[0])
st.write("Columns:", filtered_df.shape[1])

st.write(filtered_df["Churn"].value_counts())

# =========================
# KPI METRICS
# =========================
retained = (filtered_df["Churn"] == "No").sum()
churned = (filtered_df["Churn"] == "Yes").sum()
retention_rate = (retained / len(filtered_df)) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(filtered_df))
col2.metric("Retained", retained)
col3.metric("Retention %", f"{retention_rate:.1f}%")

# =========================
# CHURN DISTRIBUTION
# =========================
st.subheader("Churn Distribution")

counts = filtered_df["Churn"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(counts.index, counts.values)
ax1.set_title("Customer Churn")
st.pyplot(fig1)

# =========================
# CONTRACT ANALYSIS
# =========================
st.subheader("Churn by Contract Type")

contract_churn = pd.crosstab(filtered_df["Contract"], filtered_df["Churn"])

fig2, ax2 = plt.subplots()
contract_churn.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# =========================
# TENURE DISTRIBUTION
# =========================
st.subheader("Tenure Distribution")

fig3, ax3 = plt.subplots()
ax3.hist(filtered_df["tenure"], bins=20)
ax3.set_title("Customer Tenure Distribution")
st.pyplot(fig3)

# =========================
# INSIGHTS
# =========================
st.subheader("Key Insights")

st.write("""
- Month-to-month customers churn more often.
- Longer contracts improve retention.
- Tenure is strongly related to churn.
""")

# =========================
# RAW DATA
# =========================
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)