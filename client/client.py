import requests
BASE_URL = 'http://127.0.0.1:8000/api/'
TOKEN = 'ad69e32bfa419bdaceaa72b20823514f2c01'
headers = {'Authorization': f'Token {TOKEN}'}

# Get all polls
resp = requests.get(BASE_URL + 'polls/', headers=headers)
print(resp.status_code)
print(resp.json())
