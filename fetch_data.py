import requests
import pandas as pd

API_KEY = "7223a99ea46444635caf6e430e59a693"
SUBGRAPH_ID = "5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"
URL = f"https://gateway.thegraph.com/api/{API_KEY}/subgraphs/id/{SUBGRAPH_ID}"

# Get information of 1000 pools
def fetch_pools(skip):
    query = f"""
    {{
      pools(first: 1000, skip: {skip}, orderBy: createdAtTimestamp, orderDirection: desc) {{
        id
        token0 {{ symbol }}
        token1 {{ symbol }}
        feeTier
        createdAtTimestamp
      }}
    }}
    """
    response = requests.post(URL, json={"query": query})
    return response.json()["data"]["pools"]

# Loop to get information of 5000 pools
all_data = []
for i in range(0, 11000, 1000):
    print(f"Fetching pools {i} ~ {i+999}...")
    page = fetch_pools(skip=i)
    if not page:
        break
    all_data.extend(page)

# Save as csv file
df = pd.json_normalize(all_data)
df.to_csv("pools_information.csv", index=False)
print("save as pools_information.csv")
