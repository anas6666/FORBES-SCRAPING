import requests
import json
import os
import boto3

# URL of the JSON data
url = 'https://www.forbes.com/billionaires/page-data/index/page-data.json'
r = requests.get(url)
data = r.json()  

# Save the JSON data to a local file
local_file = 'billionaires_data.json'
with open(local_file, 'w') as json_file:
    json.dump(data, json_file)

print("JSON data saved successfully!")

# Connect to S3
s3 = boto3.client('s3')

# Upload the JSON file to S3
bucket_name = 'rawdatabillionnaire'  # Replace with your bucket name
s3_key = 'billionaires_data.json'  # The name you want to give the file in S3

s3.upload_file(local_file, bucket_name, s3_key)

print(f"JSON data uploaded to S3 bucket '{bucket_name}' with key '{s3_key}'.")
