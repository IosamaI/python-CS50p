
from ast import main
from cgitb import text

def convert(input):
   input = input.replace(":)","🙂")
   input = input.replace(":(","🙁")
   return(input)

def main():
    text =  input("enter you text: ")
    cov = convert(text)
    print(cov)

main()

