import requests
to_do_url= "https://github.com/public-apis/public-apis"
response=requests.get(url=to_do_url)
# print(response) -->Returns Status Code
# print(dir(response)) 
# print(type(response.json()))   --> Displays the response in json format.

# for key,value in response.json().items():
#     print ("\'",key,"\': ","\'",value,"\'")

print(type(response.content))

