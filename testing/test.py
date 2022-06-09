import requests

resp = requests.post("http://localhost:5000/", files={'image': open('./testing/gutdey.jpeg', 'rb')})

print(resp.json())