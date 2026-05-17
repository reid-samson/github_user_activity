# format: https://api.github.com/users/<username>/events
# I will just list the five most recent types of events from the user

import requests
import sys

username = sys.argv[1]

url = f"https://api.github.com/users/{username}/events"
response = requests.get(url)
data = None

if response.status_code == 200:
    data = response.json()
    for i in range(5):
        print(data[i]['type'])
else:
    print("Failed to find account")


