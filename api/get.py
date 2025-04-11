import requests
import json

params = {"id": 1}

getResponse = requests.get("https://jsonplaceholder.typicode.com/posts/2") # GET request

getWithParamResponse = requests.get("https://jsonplaceholder.typicode.com/posts/", params=params) # GET with params

errorHandlingResponse = requests.get("https://jsonplaceholder.typicode.com/invalid")
if errorHandlingResponse.status_code == 404:
  print("Not Found!")

print("status Code:", errorHandlingResponse.status_code)
print(json.dumps(errorHandlingResponse.json(), indent=2))