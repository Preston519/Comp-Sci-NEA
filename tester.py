import csv
with open("students.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row)
    print(list(reader))