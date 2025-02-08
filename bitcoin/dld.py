import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit("Missing command-line argument ")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error: Unable to reach API")

print(json.dumps(response.json(),indent=5))