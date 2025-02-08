# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates
# that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75%
# full.
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
# wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the
# tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is
# essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or
# ZeroDivisionError


# def main():

#     num = rounded()
#     if num <= 1:
#         print("E")
#     elif num >= 99:
#         print("F")
#     else:
#         print(f"{num}%")


# def rounded():
#     while True:

#         try:
#             x, y = input("fractions: ").split("/")
#             x = int(x)
#             y = int(y)
#             if x <= y and y != 0:
#                 return round(x / y * 100)
#         except (ValueError, ZeroDivisionError):
#             pass


# main()


def main():
    frac = input("Fraction: ")
    pct = convert(frac)
    print(gauge(pct))


def convert(fraction):
    x, y = fraction.split("/")
    if int(x)/int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return int(int(x)/int(y) * 100)


def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()