# Binance Trade Analysis & Ranking Report
### **Prepared by: Ahmad Mohamed Aslam**

---

## **Introduction**
This report presents an analysis of **90 days of historical trading data** from Binance accounts. The objective is to **rank accounts based on financial performance** using key metrics and visualize insights using a dashboard.

---

## **Approach Used**
The approach taken to solve this problem involved multiple steps:
1. **Data Preprocessing & Cleaning:**
   - Loaded the dataset and handled missing values.
   - Converted `Trade_History` from JSON-like string format into a structured DataFrame.
   - Removed invalid timestamps and formatted datetime values.
   - Classified trades into **long_open, long_close, short_open, short_close** for better analysis.

2. **Feature Engineering & Metric Calculation:**
   - Extracted key financial indicators such as **ROI, PnL, Sharpe Ratio, MDD, Win Rate, and Total Positions**.
   - Applied time-series transformations to calculate daily PnL and Sharpe Ratio.
   - Used cumulative PnL data to compute Maximum Drawdown (MDD).

3. **Ranking Algorithm:**
   - Normalized metrics using **Min-Max scaling** to bring all values into a comparable range.
   - Applied a weighted scoring system to calculate a **Composite Score**:
     - **ROI (30%)**
     - **Sharpe Ratio (30%)**
     - **Win Rate (20%)**
     - **MDD (20%)**
   - Ranked accounts based on the final Composite Score.

4. **Dashboard Development:**
   - Built an interactive **Streamlit dashboard** for users to explore the rankings and visualize financial insights.
   - Added features such as **account filtering**, **scatter plots**, and **histograms**.

---

## **Feature Engineering & Financial Metrics**
### **Key Performance Indicators:**
1. **ROI (Return on Investment)** = Profit ÷ Investment × 100
2. **PnL (Profit & Loss)** = Total realized profit
3. **Sharpe Ratio** = (Mean Daily Return ÷ Std Dev of Returns) × sqrt(252)
4. **MDD (Maximum Drawdown)** = Largest peak-to-trough decline
5. **Win Rate** = (Winning Trades ÷ Total Trades) × 100

 **All metrics were normalized** for fair ranking.

---

## **Ranking System & Composite Score**
A **weighted scoring system** was used to rank accounts based on:
- **ROI (30%)**
- **Sharpe Ratio (30%)**
- **Win Rate (20%)**
- **MDD (20%)**

**Top 20 accounts extracted based on composite scores.**

---

## **Final Results**
 **Complete results available in:** `account_metrics.csv`
 **Top 20 accounts saved in:** `top_20_accounts.csv`

---

## **Dashboard & Visualizations**
- **Top 20 Accounts Table**: Displays rankings.
- **ROI vs. Sharpe Ratio Plot**: Visualizes risk-return trade-off.
- **MDD Histogram**: Highlights drawdown distribution.
- **Win Rate Histogram**: Shows consistency in profitable trades.

**Dashboard File:** `Dashboard.py`
**Run Command:** `streamlit run Dashboard.py`

---

## **Conclusion**
3. **Top accounts are profitable but differ in risk profiles.**
2. **Normalization ensured fair ranking.**
1. **Dashboard makes performance comparison easier.**