import requests

res = requests.get('http://127.0.0.1:5000/user4/',
                   json={'name': 'lisi', 'age': 33},
                   headers={'Content-Type': 'application/json',
                            'Cookie': 'key=6AD525768103295411C2E182D1A65DE2'})



print(res.text)


