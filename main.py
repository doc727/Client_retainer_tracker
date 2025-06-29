import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load updated data
@st.cache_data
def load_data():
    return pd.read_csv("data/updated_retainer_data.csv", parse_dates=["Next Due Date"])

df = load_data()

# KPI Metrics
st.title("📊 Client Retainer Dashboard")
st.subheader("Payment & Contract Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Clients", len(df))
col2.metric("Paid", (df["Payment Status"] == "Paid").sum())
col3.metric("Overdue", (df["Payment Status"] == "Overdue").sum())

# Pie Chart: Payment Status
st.subheader("🧾 Payment Status Distribution")
status_counts = df["Payment Status"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%")
ax1.axis("equal")
st.pyplot(fig1)

# Bar Chart: Retainer Amounts
st.subheader("💰 Total Retainer by Status")
retainer_sums = df.groupby("Payment Status")["Retainer Amount"].sum()
fig2, ax2 = plt.subplots()
retainer_sums.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# Full Table
st.subheader("📋 Full Client Data")
st.dataframe(df)
