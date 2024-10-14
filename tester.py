import csv

with open('students.csv') as addresses:
    csvreader = csv.reader(addresses)
    # connection = sqlite3.connect("student.db")
    # cursor = connection.cursor()
    # cursor.executemany("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(?, ?, ?, ?, -1)", list(csvreader))
    # cursor.execute("INSERT INTO students(StudentID, Name, Address, Year, RouteID) VALUES(-1, 'Depot', ?, -1, -1)", (depot,))
    # connection.commit()
    # connection.close()
    print(list(csvreader))