import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print(f"Retrieving {url}")

# Retrieve and read the XML data from the URL
data = urllib.request.urlopen(url).read()
print(f"Retrieved {len(data)} characters")

# Parse the XML data
tree = ET.fromstring(data)

# Find all <count> elements and sum their values
counts = tree.findall('.//count')
total_sum = sum(int(count.text) for count in counts)
count_total = len(counts)

print(f"Count: {count_total}")
print(f"Sum: {total_sum}")
