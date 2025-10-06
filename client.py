# import requests
#
#
# response = requests.post("http://localhost:8000/hello")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)


import requests


response = requests.get("http://localhost:8000/greeting")

if response.ok:
    data = response.json()
    print(data)
else:
    print(response.text)

response = requests.get("http://localhost:8001/greeting")

if response.ok:
    data = response.json()
    print(data)
else:
    print(response.text)

