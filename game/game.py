import random 
import sys

while True:
    try:
        level=int(input("level: "))
        if level > 0:
            break
    except ValueError:
        pass

number_to_guess = random.randint(1, level)

while True:
    try:
        Guess = int(input("Guess: "))
        if Guess < 1:
            continue
    except ValueError:
        continue

    if  Guess > number_to_guess :
        ##print(f"Guess:{Guess}")
        print("Too large!") 
    elif  Guess < number_to_guess :
        ##print(f"Guess:{Guess}")
        print("Too small!")
    elif  Guess == number_to_guess:
        print(f"Guess:{Guess}")
        sys.exit("Just right!")
