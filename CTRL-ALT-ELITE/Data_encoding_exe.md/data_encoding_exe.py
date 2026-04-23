import csv

with open('ford_escort.csv' , newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

        