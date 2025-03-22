import requests

URL = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.delete(URL)
if(response.status_code == 200): 
    print("Successfully delete the data")
    print(response.json())
else:
    print("Failed to delete request")