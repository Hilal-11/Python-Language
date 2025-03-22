import requests

URL = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "title": "This is Hilal",
    "body": "hello i am hilal, a software engeneer in Googke/Microsoft/Mata",
    "userId": 101
}

response = requests.post(URL , json=data)
if(response.status_code == 201):
    print("POST request successfully done")
else:
    print("Failed to POST request Oops!!!")