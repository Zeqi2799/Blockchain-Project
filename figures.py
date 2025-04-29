import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file
df = pd.read_csv("pools_information.csv")

# Statistics the number of pools created each month
df['createdAtTimestamp'] = pd.to_datetime(df['createdAtTimestamp'], unit='s')
print("The earliest pool creation time:", df['createdAtTimestamp'].min())
print("The latest pool creation time:", df['createdAtTimestamp'].max())
df = df[(df['createdAtTimestamp'] >= '2024-03-01') & (df['createdAtTimestamp'] < '2025-04-01')]
df_ts = df.set_index('createdAtTimestamp')
amount_month = df_ts['id'].resample('M').count()

# Statistics of the top 10 token pairs used in transactions
df['pair'] = df['token0.symbol'] + '/' + df['token1.symbol']
token_pairs = df['pair'].value_counts().head(10)

# Statistics of fee level distribution
fee = df['feeTier'].value_counts().sort_index()

# Plot charts
plt.figure()
amount_month.plot(kind='line', marker='o')
plt.title("New liquidity pools of Uniswap V3")
plt.xlabel("Time (month)")
plt.ylabel("Number of new pools")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure()
token_pairs.plot(kind='bar')
plt.title("Top 10 token pairs")
plt.xlabel("Token pairs")
plt.ylabel("Occurrence")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

plt.figure()
fee.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Proportion of pools with different fee tiers")
plt.ylabel('')
plt.show()
