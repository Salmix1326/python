import requests


response = requests.post("http://localhost:8000/hello")

if response.ok:
    data = response.json()
    print(data)
else:
    print(response.text)