import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------------------
# 1. DATA LOADING & ROBUST CLEANING
# -------------------------------------------------------------------------
df = pd.read_csv('HistoricalQuotes.csv')

# Strip any accidental whitespace from data column names
df.columns = df.columns.str.replace(' ', '')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)

# Clean currency strings and isolate numerical float variables
for col in ['Close/Last', 'Open', 'High', 'Low']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('$', '').str.replace(' ', '').astype(float)

df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

# Engineering Time-Series Fields for Deep Historical Tracking
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.strftime('%b')
df['Price_Spread_High_Low'] = df['High'] - df['Low']
df['Daily_Return_Pct'] = df['Close/Last'].pct_change() * 100

# Compute Long-term Smoothing Technical Indicator Metrics
df['MA50'] = df['Close/Last'].rolling(window=50).mean()
df['MA200'] = df['Close/Last'].rolling(window=200).mean()

# -------------------------------------------------------------------------
# 2. COMPUTING DETAILED TEXT REPORTS (YEAR-BY-YEAR SUMMARY TABLES)
# -------------------------------------------------------------------------
yearly_summary = df.groupby('Year').agg({
    'High': 'max',
    'Low': 'min',
    'Close/Last': 'mean',
    'Volume': 'sum',
    'Price_Spread_High_Low': 'mean'
}).rename(columns={
    'High': 'Peak_Max_Price($)', 
    'Low': 'Floor_Min_Price($)', 
    'Close/Last': 'Average_Price($)', 
    'Volume': 'Total_Quantity_Sold',
    'Price_Spread_High_Low': 'Avg_Daily_Volatility($)'
})

print("\n" + "="*85)
print("             DEEP DATA SCIENCE REPORT: 10-YEAR HISTORICAL STOCK ANALYSIS")
print("="*85)
print(yearly_summary.to_string())
print("="*85 + "\n")

# Extract peak historical insight checkpoints 
most_sold_year = yearly_summary['Total_Quantity_Sold'].idxmax()
most_sold_qty = yearly_summary['Total_Quantity_Sold'].max()
highest_price_year = yearly_summary['Peak_Max_Price($)'].idxmax()
highest_price_val = yearly_summary['Peak_Max_Price($)'].max()
lowest_price_year = yearly_summary['Floor_Min_Price($)'].idxmin()
lowest_price_val = yearly_summary['Floor_Min_Price($)'].min()

print(f"-> MAXIMUM QUANTITY DEMAND BURST : Year {most_sold_year} ({most_sold_qty:,} Total Shares Sold)")
print(f"-> MAXIMUM ABSOLUTE PRICE PEAK    : Year {highest_price_year} (${highest_price_val})")
print(f"-> LOWEST DEEPEST MARKET DROP     : Year {lowest_price_year} (${lowest_price_val})\n")

# -------------------------------------------------------------------------
# 3. HIGH-DENSITY VISUALIZATION MATRIX (7 SEPARATE NON-OVERLAPPING PLOTS)
# -------------------------------------------------------------------------
# Setting up clean visualization canvas configurations
sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.max_open_warning': 0})

# --- CHART BUNDLE PART A: MACRO HISTORICAL TRENDS (3 PLOTS) ---
fig1, axes1 = plt.subplots(3, 1, figsize=(14, 16))
fig1.suptitle('PART A: MACRO TIME-SERIES AND TECHNICAL MARKET TRENDS', fontsize=14, fontweight='bold')

# Graph 1: Continuous Stock Price Fluctuation Range
axes1[0].plot(df['Date'], df['Close/Last'], color='#1f77b4', linewidth=1.5, label='Daily Close Price')
axes1[0].set_title('Graph 1: Macro Stock Price Fluctuations Timeline', fontsize=11, fontweight='bold')
axes1[0].set_ylabel('Price Range ($)', fontsize=10)
axes1[0].grid(True, linestyle=':', alpha=0.6)

# Graph 2: Technical Structural Market Trend Smoothing (Moving Averages Indicators)
axes1[1].plot(df['Date'], df['Close/Last'], color='darkgray', alpha=0.4, label='Actual Close Data')
axes1[1].plot(df['Date'], df['MA50'], color='#ff7f0e', linewidth=1.2, label='50-Day Moving Average (Short-term)')
axes1[1].plot(df['Date'], df['MA200'], color='#d62728', linewidth=1.5, label='200-Day Moving Average (Long-term)')
axes1[1].set_title('Graph 2: Structural Market Smoothing Analysis (Technical Indicators)', fontsize=11, fontweight='bold')
axes1[1].set_ylabel('Price Base ($)', fontsize=10)
axes1[1].legend(loc='upper left')
axes1[1].grid(True, linestyle=':', alpha=0.6)

# Graph 3: Linear Trading Volumes & Demand Breakout Anomalies
axes1[2].fill_between(df['Date'], df['Volume'], color='#9467bd', alpha=0.5, label='Shares Traded')
axes1[2].set_title('Graph 3: Transaction Volumes Timeline (Trading Momentum & Supply-Demand)', fontsize=11, fontweight='bold')
axes1[2].set_xlabel('Timeline Calendar Years', fontsize=10)
axes1[2].set_ylabel('Traded Share Quantity', fontsize=10)
axes1[2].grid(True, linestyle=':', alpha=0.6)

plt.subplots_adjust(hspace=0.45) # Forces crisp spacing padding gaps between graphs

# --- CHART BUNDLE PART B: AGGREGATED METRICS SUMMARY (4 PLOTS) ---
fig2, axes2 = plt.subplots(2, 2, figsize=(16, 12))
fig2.suptitle('PART B: ANNUAL METRIC AGGREGATION AND SPREAD DISTRIBUTIONS', fontsize=14, fontweight='bold')

# Graph 4: Annual Aggregated Traded Quantities Sold Bars
sns.barplot(x=yearly_summary.index, y=yearly_summary['Total_Quantity_Sold'], ax=axes2[0, 0], palette='flare')
axes2[0, 0].set_title('Graph 4: Total Aggregated Quantity Sold (Shares) Per Year', fontsize=11, fontweight='bold')
axes2[0, 0].set_xlabel('Year')
axes2[0, 0].set_ylabel('Total Shares Traded Volume')
axes2[0, 0].tick_params(axis='x', rotation=35) # Slants labels to prevent word overlaps

# Graph 5: Yearly Stock Volatility Distribution Spread
sns.boxplot(x='Year', y='Close/Last', data=df, ax=axes2[0, 1], palette='crest')
axes2[0, 1].set_title('Graph 5: Yearly Statistical Pricing Distributions & Volatility Ranges', fontsize=11, fontweight='bold')
axes2[0, 1].set_xlabel('Year')
axes2[0, 1].set_ylabel('Price Range Variations ($)')
axes2[0, 1].tick_params(axis='x', rotation=35)

# Graph 6: Mean Pricing Margins Compared to Peak Pricing Points
axes2[1, 0].plot(yearly_summary.index, yearly_summary['Peak_Max_Price($)'], marker='o', color='red', label='Annual Peak High')
axes2[1, 0].bar(yearly_summary.index, yearly_summary['Average_Price($)'], color='lightblue', alpha=0.7, label='Annual Mean Price')
axes2[1, 0].set_title('Graph 6: Mean Annual Value vs Absolute High Price Ceilings', fontsize=11, fontweight='bold')
axes2[1, 0].set_xlabel('Year')
axes2[1, 0].set_ylabel('Asset Valuation Scale ($)')
axes2[1, 0].legend()
axes2[1, 0].tick_params(axis='x', rotation=35)

# Graph 7: Intraday Pricing Spreads (Tracking True Systemic High-Low Price Shifts)
sns.barplot(x=yearly_summary.index, y=yearly_summary['Avg_Daily_Volatility($)'], ax=axes2[1, 1], palette='magma')
axes2[1, 1].set_title('Graph 7: Average Annual Intraday Price Spreads (High vs Low Deviation)', fontsize=11, fontweight='bold')
axes2[1, 1].set_xlabel('Year')
axes2[1, 1].set_ylabel('Mean Intraday Spread Deviation ($)')
axes2[1, 1].tick_params(axis='x', rotation=35)

plt.subplots_adjust(hspace=0.4, wspace=0.3) # Controls safe spacing margins across coordinate axes matrices
plt.show()