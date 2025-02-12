#  Binance Trading Performance Analysis

##  Project Overview
This project analyzes **90 days of historical trading data** from multiple Binance accounts to evaluate performance using key financial metrics. The goal is to **rank the top 20 accounts** based on profitability, risk management, and consistency, and present the findings using an interactive dashboard.

---

##  Dataset Information
The dataset contains:
- **Port_IDs**: Unique identifiers for accounts.
- **Trade_History**: List of historical trades, including timestamp, asset, side (BUY/SELL), price, and realized profit.
- **Additional Fields**: Position classification (long/short), quantity traded, and more.

 **Dataset Provided:** [`TRADES_CopyTr_90D_ROI.csv`](#)

---

##  Objectives
1. **Data Cleaning & Preprocessing**
   - Handle missing values and parse trade history.
   - Convert timestamps to readable format.
   - Classify trades based on position type.

2. **Feature Engineering & Metric Calculation**
   - Compute key financial metrics: **ROI, PnL, Sharpe Ratio, MDD, Win Rate, Total Positions**.
   - Normalize metrics for fair ranking.
   
3. **Ranking Algorithm**
   - Develop a **composite score** using weighted metrics.
   - Rank the top 20 accounts based on performance.
   
4. **Dashboard Visualization**
   - Build an interactive **Streamlit dashboard** to explore rankings and metrics.

---

##  How to Run the Project
### **1. Run the Jupyter Notebook for Analysis**
```bash
jupyter notebook Binance_Trading_Accounts_Analysis.ipynb
```

### **2. Run the Streamlit Dashboard**
```bash
streamlit run Dashboard.py
```

---

## Dashboard Features
- **Top 20 Accounts**: View ranked accounts based on performance.
- **ROI vs. Sharpe Ratio Scatter Plot**: Visualizes risk-adjusted returns.
- **Maximum Drawdown Histogram**: Shows risk distribution.
- **Win Rate Distribution**: Displays consistency of profitable trades.
- **Account Filtering**: Select and analyze individual account performance.

 **Dashboard File:** `Dashboard.py`

---

##  File Structure
```
/Trading_Performance_Analysis
│── Binance_Trading_Accounts_Analysis.ipynb                     # Jupyter Notebook for data analysis
│── Dashboard.py                                                # Streamlit Dashboard
│── account_metrics.csv                                         # All calculated metrics
│── top_20_accounts.csv                                         # Top-ranked accounts
│── report.md                                                   # Full project report
│── README.md                                                   # Quick project guide 
│──TRADES_CopyTr_90D_ROI.csv                                    # The Dataset provided
```



