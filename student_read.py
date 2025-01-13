import sqlite3

#select the selected student detail
def retrieve_students():
    try:
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        #fetch all data from table in SQL db
        cursor.execute("SELECT * FROM students")
        #store all fetched data inside results variable
        students = cursor.fetchall()
        print("Students retrieved successfully.")
        return students

    except sqlite3.Error as e:
        print("Error", e)
        return None

    finally:
        cursor.close()
        connection.close()

students = retrieve_students()
if students:
    for student in students:
        print(student)
else:
    print("No students found.")