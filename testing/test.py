import requests

resp = requests.post("http://localhost:5000/", files={'image': open('./testing/kertas-baru.jpeg', 'rb')})

print(resp.json())