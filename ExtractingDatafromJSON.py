import urllib.request
import json

# Prompt for the URL
url = input('Enter location: ')

# Read the JSON data from the URL
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

if not js or 'comments' not in js:
    print('Failed to retrieve or parse JSON data')
    quit()

# Extract comment counts and compute the sum
comments = js['comments']
count = len(comments)
sum_counts = sum(int(comment['count']) for comment in comments)

# Output the results
print('Retrieved', len(data), 'characters')
print('Count:', count)
print('Sum:', sum_counts)
