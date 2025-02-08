# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

   
# def is_valid(s):
#     # Length check
#     if not (2 <= len(s) <= 6):
#         return False

#     # First two characters must be letters
#     if not s[:2].isalpha():
#         return False

#     # Check for invalid characters
#     if not s.isalnum():
#         return False

#     # Initialize a flag to track if a number has been encountered
#     number_encountered = False

#     for i, char in enumerate(s):
#         if char.isdigit():
#             # Check if the first number is '0'
#             if char == '0' and i == 2:
#                 return False

#             number_encountered = True 

#         if char.isalpha() and number_encountered:
#             # If a letter appears after a number, it's invalid
#             return False

#     return True





# main()



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        # Return true if characters are all letters
        if s.isalpha():
            return True
        else:
            # Check for number in the middle
            # (only if the first two characters are letters and the last character is number)
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        # Return false if number starts with 0 or the following character is letter
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()