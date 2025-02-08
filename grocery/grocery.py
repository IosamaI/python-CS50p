

try:
    # Initialize an empty dictionary to store items and their counts
    grocery_items = {}

    while True:
        # Prompt the user for an item
        item = input("")

        # Convert the item to uppercase for case-insensitivity
        item = item.upper()

        # Update the dictionary with the item count
        if item in grocery_items:
            grocery_items[item] += 1
        else:
            grocery_items[item] = 1

except EOFError:
    # Sort the items alphabetically
    sorted_items = sorted(grocery_items.keys())

    # Print the sorted list of items with their counts
    
    for item in sorted_items:
        print(f"{grocery_items[item]} {item}")

