import requests
import json

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

# print("start")
# URL = "https://api.sampleapis.com/jokes/goodJokes"

# response = requests.get(URL)
# if response.status_code == 200 :
#     print("Retreive data from server successfully")
#     try:
#         with open("jokes.json" , "w") as f:
#             json.dump(response.json() , f , indent=4)
#     except:
#         print("Failed to fetch data form api and generate a json file")
#     print(response.json())
# else:
#     print("Failed to get data from server") 
    
# print("end")  


URL = "https://api.sampleapis.com/jokes/goodJokes"

def fetchDataFromServer() :
    response = requests.get(URL)
    if(response.status_code == 200) :
        print("Retreive data from server successfully")
        print(response.json())
    else:
        print("Failed to fetch data from server")

fetchDataFromServer()