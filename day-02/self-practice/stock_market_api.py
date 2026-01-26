import requests

API_KEY="P4QH87SB8IJNU662" #Getting the API-key

api_url="https://www.alphavantage.co/" #Extracting the base URL

symbol="AMZN"

function="TIME_SERIES_DAILY"

interval="5min"

query=f"query?function={function}&symbol={symbol}&apikey={API_KEY}" #seperating the query for clear understanding purpose and making code readability

# print(api_url+query) --> Prints the api after concatenating it with the query

response=requests.get(api_url+query)
# print(response.json())

for key,value in response.json().items():
    for i in value:
        if i > 200.00:
            print(key,value)