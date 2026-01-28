import requests

bitcoin_url =""
response=requests.get(url=bitcoin_url)
print(response.json())