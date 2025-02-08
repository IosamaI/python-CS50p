import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if all(0 <= int(ip.group(i)) <= 255 for i in range(1,5)):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()

























# import re
# import sys


# def main():
#     try:
#         ip = input("IPv4 Address: ")

#         num1,num2,num3,num4 = ip.split(".")

#         if int(num1) <= 255 and int(num2) <= 255 and int(num3) <= 255 and int(num4) <= 255 :
#             validate(ip)
#         else:
#             sys.exit("False")
#     except ValueError:
#         sys.exit("False")


# def validate(ip):
   
#     if re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
#        print("True")

#     else:
#        print("False")

   
    


  


if __name__ == "__main__":
    main()