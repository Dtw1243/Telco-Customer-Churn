import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Telco Customer Churn Dashboard")

data = pd.read_csv("Telco Customer Retention CSV.csv")

# setting up a section header and displaying the first few rows of the dataframe
st.subheader("Customer Churn Overview")
st.dataframe(data.head())


st.write("Rows: ", data.shape[0])
st.write("Columns: ", data.shape[1])

st.write(data.dtypes)

# displaying the value counts of the "Churn" column
st.write(data["Churn"].value_counts())

retained = (data["Churn"] == "No").sum()
churned = (data["Churn"] == "Yes").sum()

retention_rate = (retained / len(data)) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(data))
col2.metric("Retained", retained)
col3.metric("Retention %", f"{retention_rate:.1f}%")

# setting up and creating a chart to visualize the churn distribution
st.subheader("Churn Distribution")

counts = data["Churn"].value_counts()

fig, ax = plt.subplots()

ax.bar(
    counts.index,
    counts.values
)

ax.set_title("Customer Churn")

st.pyplot(fig)

# making the chart interactive by allowing users to filter the data based
contract_type = st.sidebar.selectbox(
    "Contract Type",
    data["Contract"].unique()
)

filtered_df = data[
    data["Contract"] == contract_type
]

#1. Load CSV
#2. Preview data
#3. Understand columns
#4. Create KPI cards
#5. Create first chart
#6. Add filters
#7. Add more charts
#8. Improve layout
#9. Deploy to Streamlit Cloud

#adding more filters
# answers Which contract types lose the most customers?
contract_churn = pd.crosstab(
    data["Contract"],
    data["Churn"]
)

st.bar_chart(contract_churn)

#answers Which tenure groups lose the most customers?
st.subheader("Tenure Distribution")
fig, ax = plt.subplots()

ax.hist(
    data["tenure"],
    bins=20
)

st.pyplot(fig)

#creating an understanding of the data that is more interactive and allows users to filter the data based on multiple criteria
st.subheader("Key Insights")

st.write("""
- Customers with month-to-month contracts churn more often.
- Long-term customers have higher retention.
- Higher monthly charges appear correlated with churn.
""")

#editing the layout of the dashboard to make it more visually appealing and user-friendly
st.sidebar.header("Filters")
col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)


# allowing for the addition of more charts to visualize the data in different ways
st.subheader("Additional Charts")

if st.checkbox("Show Raw Data"):
    st.dataframe(data)

