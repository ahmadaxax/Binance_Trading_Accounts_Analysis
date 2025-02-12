import streamlit as st
import pandas as pd
import plotly.express as px

metrics_df = pd.read_csv("account_metrics.csv")
top_20_accounts = pd.read_csv("top_20_accounts.csv")

st.title("📊 Trading Performance Dashboard")

# Display the top 20 ranked accounts in a table format
st.subheader("🏆 Top 20 Accounts")
st.dataframe(top_20_accounts)

# Scatter plot to analyze ROI vs. Sharpe Ratio
st.subheader("📈 ROI vs. Sharpe Ratio")
fig = px.scatter(
    metrics_df,
    x="ROI",
    y="Sharpe_Ratio",
    size=metrics_df["MDD"].abs(),  
    color="Composite_Score",
    hover_data=["Port_IDs", "Win_Rate"],
    title="ROI vs. Sharpe Ratio (Size by MDD)"
)
st.plotly_chart(fig)

# Histogram to show the distribution of Maximum Drawdown across accounts
st.subheader("📉 Maximum Drawdown Distribution")
fig_mdd = px.histogram(
    metrics_df, x="MDD", nbins=20, title="Distribution of Maximum Drawdowns"
)
st.plotly_chart(fig_mdd)

# Histogram to show Win Rate distribution
st.subheader("🏅 Win Rate Distribution")
fig_win_rate = px.histogram(
    metrics_df, x="Win_Rate", nbins=20, title="Distribution of Win Rates"
)
st.plotly_chart(fig_win_rate)

# Dropdown to allow filtering for a specific account
st.subheader("🔍 Filter Accounts")
selected_port_id = st.selectbox("Select Account ID", metrics_df["Port_IDs"].unique())
account_data = metrics_df[metrics_df["Port_IDs"] == selected_port_id]
st.write(account_data)
