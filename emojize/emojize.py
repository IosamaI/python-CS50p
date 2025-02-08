import emoji

# Prompt the user for input
n = input("input:")

# Convert the emoji codes to their corresponding emojis
m = emoji.emojize(n,language='alias')

# Print the emojized string
print(m)
