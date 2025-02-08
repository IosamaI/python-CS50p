def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x= int(x)
    z= int(z)
    result= calculate(x,y,z)
    print(f"{result:.1f} ")

def calculate(x,y,z):
    match y:
        case "+" :
            return x+z
        case "/":
            return x/z
        case "*":
            return x*z
        case "-":
            return x-z
        case _:
            return 0


main()