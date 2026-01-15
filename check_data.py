import pandas as pd

df = pd.read_csv("data/telco_churn.csv")
print(df.head())
print("\nTotal Rows:", len(df))
