import sqlite3

#Creating lecturer table
connection = sqlite3.connect('lecturers.db')
cursor = connection.cursor()
sql_command = '''CREATE TABLE IF NOT EXISTS lecturers (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    course TEXT,
                    department TEXT)'''
cursor.execute(sql_command)
connection.close()








