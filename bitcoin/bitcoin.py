import requests
import sys

if len(sys.argv)!=2:
    sys.exit("Missing command-line argument ")

try:
    bitcoins =float(sys.argv[1])
    
except ValueError:
    sys.exit("Error: Argument must be a float")

    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error: Unable to reach API")

data = response.json()
price = data['bpi']['USD']['rate_float']

total_cost = price * bitcoins

print(f"${total_cost :,.4f}")