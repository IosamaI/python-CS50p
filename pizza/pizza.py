import sys
import csv
import os
from tabulate import tabulate



if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".csv"):
    sys.exit("Not a CSV file")
    
elif sys.argv[1].lower().endswith("sicilian.csv"):
      with open("sicilian.csv") as file1:
            reader1 = csv.reader(file1)
            print(tabulate(reader1,headers="firstrow", tablefmt="grid"))


elif sys.argv[1].lower().endswith("regular.csv"):
      with open("regular.csv") as file2:
            reader2 = csv.reader(file2)
            print(tabulate(reader2,headers="firstrow", tablefmt="grid"))
               



elif os.path.exists(sys.argv[1]):
    sys.exit("File exists")
else:
    sys.exit("File does not exist")

    

   