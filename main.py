import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url).json()
# print(response.status_code)
# users=response.json()
# # print(users[0]['id'])  # Print the ID of the first user
# # for use in users:
# #     print(use['name'])  # Print the name of each user
# #     print(use['email'])  # Print the email of each user
# #     print(use['address']['city'])  # Print the city of each user's address
# result=pd.DataFrame(users)  # Convert the list of users to a DataFrame
# print(result)  # Print the DataFrame
df = pd.DataFrame(response)  # Convert the list of users to a DataFrame

print(df)
df.to_csv('users.csv', index=False)  # Save the DataFrame to a CSV file
print("Data saved to users.csv")  # Print a message indicating that the data has been saved
df.to_excel('users.xlsx', index=False)  # Save the DataFrame to an Excel file
print("Data saved to users.xlsx")  # Print a message indicating that the data has been