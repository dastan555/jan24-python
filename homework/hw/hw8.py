from pprint import pprint 
import requests

# headers = {"content-type": "application/json"}
digital_url = "https://status.digitalocean.com/api/v2/status.json"

response = requests.get(url=digital_url, headers={"content-type": "application/json"})
response.json = response.json()

print("Id:", (response.json["page"]["id"]))
print("Name:", (response.json["page"]["name"]))
print("Time Zone:", (response.json["page"]["time_zone"]))
print("Updated:", (response.json["page"]["updated_at"]))
print("Status:", (response.json["status"]["description"]))
# pprint(response.json)