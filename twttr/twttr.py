# def main ():
#     text = input("input: ")
#     text = text.strip()
#     remove_vowels(text)


# def  remove_vowels(text):
#     vowels = "aeiouAEIOU"
#     rez=''
#     rez=rez.strip()

#     for i in text:
#         if i  in vowels:
#             continue
#         else:
#             rez = rez + i

#     print("output:",rez)

# #if "__name__" == "__main__":
# main()



def main():
    text = input("Input: ")
    result = shorten(text)
    print("Output:", result)

def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()

