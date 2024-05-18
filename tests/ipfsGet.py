import requests

url = 'http://127.0.0.1:5001/api/v0/cat'
params = {
    'stream-channels': 'true',
    'encoding': 'json',
    'arg': 'QmUjE3kn917vN12GJgG4FhMfuvWXhfJvynq8nGBcFs8bmH'
}

response = requests.post(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    response.raise_for_status()
