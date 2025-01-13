import sqlite3
# creating students table
connection = sqlite3.connect('students.db')
cursor = connection.cursor()
sql_command = '''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    email TEXT,
                    student_number INTEGER,
                    course TEXT)'''
cursor.execute(sql_command)
connection.close()






















