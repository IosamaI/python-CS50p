import random
import sys
def main():
        level = get_level()
        score = 0

        for i in range(10):
            if i == 10:
                sys.exit
            x=generate_integer(level)
            y=generate_integer(level)
            correct_answer = x + y

            for attempt in range(3):
                try:
                    user_ans=int(input(f"{x} + {y} = "))
                    if user_ans == correct_answer:
                        score = score + 1
                        break

                    else:
                        print("EEE")

                except ValueError:
                    print("EEE")

            else:
                 print(f"{x} + {y} = {correct_answer}")

    
        print(f"{score}")


       ## user_input = input("Do you want to continue? (yes/no) ")
    ## if user_input.lower() == "no":
      ##       break    
       ## else:
         ##   continue

def get_level():
    while True:
        try:

            level = int(input())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level < 1 or level > 3:
        raise ValueError("Invalid level")
    
    elif level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

    ##min_val = 10 ** (level - 1)
    ##max_val = (10 ** level) - 1
    ##return random.randint(min_val, max_val)


if __name__ == "__main__":
    main()