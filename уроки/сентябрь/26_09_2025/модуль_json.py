import json

users = [
    {'login': 'admin', 'password': 'ыволпрывп'},
    {'login': 'user1', 'password': 'ывпывп'},
]


with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)


with open('users.json', 'r') as f:
    users = json.load(f)
    print(users)