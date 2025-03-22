import requests

URL = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    "id": 12,
    "title": "React Devs",
    "body": "Updated body content",
    "userId": 12
}
response = requests.put(URL , json=data)
if(response.status_code == 200):
    print("Succssfully update the data")
    print(response.json())
else:
    print("Failed to update the data")
    print(response.status_code)