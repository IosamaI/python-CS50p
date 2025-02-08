import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # No command-line arguments provided, use a random font
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        # Two command-line arguments provided
        font = sys.argv[2]
        if font not in available_fonts:
            print(f"Error: '{font}' is not a valid font.")
            sys.exit(1)
    else:
        print("Usage: figlet.py [-f FONT | --font FONT]")
        sys.exit(1)

    # Set the font
    figlet.setFont(font=font)

    # Prompt the user for text input
    text = input("Enter a string: ")

    # Output the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
cd