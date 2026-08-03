import requests
import pandas as pd
import numpy as np
import pandas as pd

# Load customer data
customers = pd.read_csv("customers.csv")

# Invalid ages
invalid_age = customers[
    (customers["age"] < 0) |
    (customers["age"] > 120)
]

# Duplicate IDs
duplicates = customers[
    customers.duplicated(
        subset="id",
        keep=False
    )
]

# Invalid emails
invalid_email = customers[
    ~customers["email"].str.contains(
        r"^[\w\.-]+@[\w\.-]+\.\w+$",
        regex=True
    )
]

# Invalid phone numbers
invalid_phone = customers[
    ~customers["phone"].str.match(r"^07\d{9}$")
]

print("Invalid Ages")
print(invalid_age)

print("Duplicate IDs")
print(duplicates)

print("Invalid Emails")
print(invalid_email)

print("Invalid Phones")
print(invalid_phone)
