import requests
import json

# Make the GET request to the API
response = requests.get("https://anapioficeandfire.com/api/characters/583")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Format and print the JSON data
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")