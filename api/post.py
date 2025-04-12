import requests
import json

data = {"title": "New Post", "body": "Hello World", "userId": 1}
headers = {"Content-Type": "application/json"}

response = requests.post(
  "https://jsonplaceholder.typicode.com/posts/",
  json=data,
  headers=headers
)

print("status Code:", response.status_code)
print(json.dumps(response.json(), indent=2))