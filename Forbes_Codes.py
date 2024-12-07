import requests
import json

# URL of the JSON data
url = 'https://www.forbes.com/billionaires/page-data/index/page-data.json'
response = requests.get(url)
data = response.json()

# Save the JSON data to a local file
local_file = 'billionaires_data.json'
with open(local_file, 'w') as json_file:
    json.dump(data, json_file)

print("JSON data saved successfully!")
