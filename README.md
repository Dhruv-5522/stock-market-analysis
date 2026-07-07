# Historical Stock Market Analysis (Apple Inc.)

A comprehensive 10-year data analysis project investigating historical stock performance, macro price trends, market liquidity, and asset volatility. This project utilizes Python data science tools to clean, aggregate, and visualize multi-year stock records.

## Project Objectives
* **Trend Analysis:** Map structural stock price movements over a 10-year timeline.
* **Supply & Demand:** Evaluate annual transaction volumes to pinpoint peak market activity.
* **Volatility Mapping:** Track intraday price spreads and yearly valuation boundaries.
* **Technical Indicators:** Apply short-term (50-day) and long-term (200-day) Moving Averages to analyze baseline support levels.

---

## Core Analytical Insights

### 1. Market Value & Price Ceilings
* **Peak Valuation:** The stock achieved its highest historic momentum ceiling during 2020, reaching over $320.
* **Deep Market Drops:** The lowest market floor was recorded back in 2010, trading under $50, establishing a major long-term growth curve over the decade.
* **Valuation Growth:** The annual mean price closely followed the upper ceilings, showing stable asset appreciation.

### 2. Trading Quantities & Market Demand
* **Liquidity Spike:** Maximum market demand and trading volumes peaked heavily between 2010 and 2012, showing immense trading interest.
* **Volume Tapering:** While prices continued expanding upward toward 2020, total annual shares traded gradually leveled off, suggesting a shift toward high-value holding patterns.

### 3. Volatility & Spread Deviations
* **Intraday Spreads:** Daily price volatility (High vs. Low margins) was tightest during the early years (2010–2014).
* **Late-Stage Volatility:** Intraday price swing margins grew significantly in 2018 and reached an absolute peak in 2020, indicating sharp day-to-day market sensitivity.

---

## Technical Visualizations
The code generates structured visual plots divided into two analytical sections:

1. **Timeline Patterns (Part A):** Contains continuous stock price fluctuations, technical indicator tracking curves (50-day and 200-day moving averages), and liquidity transaction timelines.
2. **Annual Aggregations (Part B):** Contains year-by-year volume distributions, statistical boxplots showing pricing spreads, and high-low boundary comparisons.

---

## Tech Stack Used
* **Language:** Python
* **Environment:** VS Code / Jupyter
* **Libraries:** Pandas, Matplotlib, Seaborn

## How to Run the Analysis
1. Place the dataset `HistoricalQuotes.csv` in the root directory.
2. Run the main execution file:
   ```bash
   python stock_anaylis.py# stock-market-analysis
