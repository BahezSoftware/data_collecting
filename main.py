import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params)

print(response.status_code)
data = response.json()
print(data[0])
import pandas as pd

df = pd.DataFrame(data)

print(df.head())

df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes
df["name"] = df["name"].str.strip()
df["symbol"] = df["symbol"].str.upper()
df["last_updated"] = pd.to_datetime(df["last_updated"])
df["current_price"] >= 0
df["current_price"] >= 0
df.isnull().sum()
df.dropna()
df.fillna(0)
df["current_price"] = df["current_price"].fillna(
    df["current_price"].mean()
)
df.drop_duplicates()
df.drop_duplicates(subset="id")
df["current_price"].mean()

df["market_cap"].max()

df["current_price"].min()
import numpy as np

np.mean(df["current_price"])

np.max(df["market_cap"])
import numpy as np

np.mean(df["current_price"])

np.max(df["market_cap"])
df.to_csv("coins.csv", index=False)