import requests 
import json


def api_response():
    api_url ="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url=api_url) # Returns the status code 
    content=response.json() #Stores data in form of list inside the variable content
    # print(content)
    print(type(content)) #Proves that the content is of type list
    target_key='body'   # Variable for storing the key of the data which we want to extract
    body_list=[]   # Creating a new list that can store the extracted data 
    for item in content:  #For each dictionary present inside list (i.e. inside content)
        if target_key in item:  
            body_list.append(item[target_key])  # Stores the value inside new list (i.e. body_list)
    return body_list #function returns the new list

output=api_response()
# print(output)
# print(type(output))
# print(output[0])

with open('output.json','w') as json_file:
    json.dump(output, json_file)
