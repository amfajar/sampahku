import requests
x = 10
while x > 0:
    
    resp = requests.post("https://sampahku-ml-api-r5feak6qfq-et.a.run.app:8080", files={"image": open("./rokok.jpeg", "rb")})
    print(resp.json())
    x -= 1