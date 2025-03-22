import requests

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

URL = "https://api.sampleapis.com/jokes/goodJokes"

response = requests.get(URL)
if response.status_code == 200 :
    print("Retreive data from server successfully")
    print(response.json())
else:
    print("Failed to get data from server")