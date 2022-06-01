import requests
x = 10
while x > 0:
    
    resp = requests.post("http://localhost:5000", files={"image": open("rokok.jpeg", "rb")})
    print(resp.json())
    x -= 1