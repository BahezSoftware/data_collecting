import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}

response = requests.get(url, params=params).json()
df = pd.DataFrame(response)
# print(df)
coins = df[
    [
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "price_change_percentage_24h"
    ]
]

print(coins)
expensive = coins[coins["current_price"] > 1000]

print(expensive)
sorted_df = coins.sort_values(
    by="current_price",
    ascending=False
)

print(sorted_df)