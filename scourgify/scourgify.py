import sys
import csv

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv":
        try:
             open(sys.argv[1])
        except FileNotFoundError:
            exit(f"Could not read {sys.argv[1]}")

        else:
            list = []
            with open(sys.argv[1]) as file1:
                reader1 = csv.DictReader(file1)
                for row in reader1:
                    name,house = row
                    first_name, last_name= row["name"].split(', ')
                    list.append({"first":first_name,"last":last_name,"house":row[house]})

            with open(sys.argv[2], "w") as file2:  
                writer= csv.DictWriter(file2, fieldnames=["first", "last","house"])
                writer.writeheader()
                for row in list:
                    writer.writerow(row)
        
