## Code Overview
- fetch_data.py 
  Fetches liquidity pool data from Uniswap V3 using The Graph API, including token pairs, fee tiers, and creation timestamps. Saves the result as `pools_information.csv`.
  
- clean_data.py
  Cleans and filters the raw data by removing missing values and selecting pools created between March 2024 and April 2025. Outputs the cleaned dataset as `cleaned_pools.csv`.
  
- figures.py 
  Analyzes and visualizes the cleaned data. Generates plots showing the monthly number of new pools, the top 10 most frequent token pairs, and the distribution of fee tiers.


## Team Contribution
Each team member completed 1/3 of the total project workload. The general contents are:

- Yuhui Jiao: Stated the main goals and steps of the project. Organized the relevant concepts of Uniswap V3 and explained key functions and core events in the Factory Contract.
  
- Zeqi Chen: Wrote Python scripts to query liquidity pool data, collected and processed raw data from The Graph, and analyzed and summarized liquidity trends over the past year.
  
- Yuchen Zheng: Wrote Python scripts to clean liquidity pool data and used LLM to forecast transaction trends for April 2025. Also formatted and organized the final report.
