import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()
response = cursor.execute("SELECT Address FROM students")
print(list(map(lambda x: x[0], response.fetchall())))