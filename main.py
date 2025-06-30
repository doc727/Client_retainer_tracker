import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/updated_retainer_data.csv", parse_dates=["Payment Date", "Next Due Date"])
    return df

df = load_data()

# ----------------------------
# 🔍 SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("🔍 Filter Data")

status_filter = st.sidebar.multiselect(
    "Select Payment Status",
    options=df["Payment Status"].unique(),
    default=df["Payment Status"].unique()
)

contract_filter = st.sidebar.multiselect(
    "Select Contract Status",
    options=df["Contract Status"].unique(),
    default=df["Contract Status"].unique()
)

# Apply filters
df_filtered = df[
    (df["Payment Status"].isin(status_filter)) &
    (df["Contract Status"].isin(contract_filter))
]

# ----------------------------
# 🔢 KPI METRICS
# ----------------------------
st.title("📊 Client Retainer Dashboard")
st.subheader("Payment & Contract Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Clients", len(df_filtered))
col2.metric("Paid", (df_filtered["Payment Status"] == "Paid").sum())
col3.metric("Overdue", (df_filtered["Payment Status"] == "Overdue").sum())

# ----------------------------
# 🥧 PIE CHART: Payment Status
# ----------------------------
st.subheader("🧾 Payment Status Distribution")
status_counts = df_filtered["Payment Status"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
ax1.axis("equal")
st.pyplot(fig1)

# ----------------------------
# 📊 BAR CHART: Retainer by Status
# ----------------------------
st.subheader("💰 Total Retainer by Payment Status")
retainer_sums = df_filtered.groupby("Payment Status")["Retainer Amount"].sum()
fig2, ax2 = plt.subplots()
retainer_sums.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Total Retainer ($)")
st.pyplot(fig2)

# ----------------------------
# 📈 LINE CHART: Monthly Paid Income
# ----------------------------
st.subheader("📈 Monthly Retainer Collection Trend")

df_filtered["Month"] = df_filtered["Payment Date"].dt.to_period("M").astype(str)
monthly_income = df_filtered.groupby("Month")["Paid Amount"].sum().reset_index()

fig3, ax3 = plt.subplots()
ax3.plot(monthly_income["Month"], monthly_income["Paid Amount"], marker="o")
ax3.set_xlabel("Month")
ax3.set_ylabel("Total Paid ($)")
ax3.set_title("Monthly Retainer Income")
st.pyplot(fig3)

# ----------------------------
# 📊 BAR CHART: Top Paying Clients
# ----------------------------
st.subheader("💼 Top Paying Clients")

top_clients = df_filtered.groupby("Client Name")["Paid Amount"].sum().sort_values(ascending=False).head(10)
fig4, ax4 = plt.subplots()
top_clients.plot(kind="bar", ax=ax4)
ax4.set_ylabel("Total Paid ($)")
ax4.set_title("Top 10 Paying Clients")
st.pyplot(fig4)

# ----------------------------
# 📋 Full Table View
# ----------------------------
st.subheader("📋 Client Data Table")
st.dataframe(df_filtered)
