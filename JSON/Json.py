import json
# data = [
#     {
#         "name": "Alex C",
#         "age": 2,
#         "city": "Houston"
#     },
#     {
#         "name": "John G",
#         "age": 40,
#         "city": "Washington"
#     },
#     {
#         "name": "Bala T",
#         "age": 22,
#         "city": "Bangalore"
#     }
# ]

data = {
    "name": "John G",
    "age": 40,
    "city": "Washington"
}
print(type(data))
print(data["name"])
print(data["age"])
print(data["city"])

y = json.dumps(data)
print(type(y))