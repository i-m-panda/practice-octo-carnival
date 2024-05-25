import requests

r = requests.get('https://api.github.com/users')
r.status_code
print(r.json())