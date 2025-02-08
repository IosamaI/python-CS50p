# text = input("Greeting: ")
# text = text.lower()
# text = text.lstrip()


# if   text.startswith("hello"):
#     print("$0")
# elif   text.startswith("h"):
#     print("$20")
# else:
#     print("$100")

def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
