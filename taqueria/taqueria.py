


d={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
n = 0
while True:
    try:
        item = input("item:").title()
        if item in d :
            to = d.get(item)
            n = n + to
            print(f"Total:${n:.2f}")

    except EOFError:
        break