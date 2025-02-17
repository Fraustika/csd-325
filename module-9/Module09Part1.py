
# Code snippet number 1
# Testing Google and Astros API

import requests

response = requests.get('http://www.google.com')
print(response.status_code)
   
   # Test the connection
response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)

   # Print response no format
print(response.json())

   # Print the formatted response
data = response.json()
print("Number of astronauts in space:", data['number'])
for person in data['people']:
    print(f"{person['name']} is on the {person['craft']}")