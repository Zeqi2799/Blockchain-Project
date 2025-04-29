import pandas as pd

# Read the original csv file
df = pd.read_csv("pools_information.csv")
df['createdAtTimestamp'] = pd.to_datetime(df['createdAtTimestamp'], unit='s')
df['createdAtDate'] = df['createdAtTimestamp'].dt.date

# Keep valid data
df_cleaned = df.dropna(subset=['token0.symbol', 'token1.symbol'])
df_filtered = df_cleaned[(df_cleaned['createdAtTimestamp'] >= '2024-03-01') & (df_cleaned['createdAtTimestamp'] <= '2025-04-01')]

# Construct readable table
df_filtered['pair'] = df_filtered['token0.symbol'] + '/' + df_filtered['token1.symbol']
output = df_filtered[['createdAtDate', 'pair', 'feeTier']]

# Save as a new csv file
output.to_csv("cleaned_pools.csv", index=False)
print("save as cleaned_pools.csv")
