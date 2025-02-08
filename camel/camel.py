
def main():
    camel_case_str = input("camelCase: ")
    camel_case_str = camel_case_str.strip()

    camel_case_str = camel_to_snake(camel_case_str)

    print("snake_case: ",camel_case_str)




def camel_to_snake(camel_case_str):

    """
    Converts a camel case string to snake case.
    """
    
    snake_case_str = ' '
    snake_case_str  =   snake_case_str.strip()
    
    for c in camel_case_str:
        # If the character is uppercase, add an underscore and lowercase the character
        if c.isupper():
            snake_case_str += '_' + c.lower()
        else:
            snake_case_str += c
    
    return snake_case_str

main()