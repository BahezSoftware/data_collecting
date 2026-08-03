import requests
import pandas as pd
import numpy as np

sales = np.array([120, 150, 180, 210, 175])

print(sales)
np.mean(sales)
np.median(sales)
random_sales = np.random.randint(100, 1000, 10)
print(random_sales)
sales = np.random.randint(500, 5000, 30)

print("Daily Sales")
print(sales)

print("\nAverage Sales")
print(np.mean(sales))

print("\nHighest Sale")
print(np.max(sales))

print("\nLowest Sale")
print(np.min(sales))

print("\nMedian Sale")
print(np.median(sales))