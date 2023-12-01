import requests
# pip install requests

# GET请求
res = requests.get('http://127.0.0.1:5000/request/?name=lisi&name=wangwu&age=33',
                    cookies={'name': 'hello'})
print(res.text)

# POST请求
# res = requests.post('http://127.0.0.1:5000/request/',
#                     data={'name': 'lucy', 'age': 33})
# print(res.text)

