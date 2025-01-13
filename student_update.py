import sqlite3

#updates the current student details

def update_student(id, name, surname, email, student_number, course):
    try:
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name=?, surname=?, email=?, student_number=?, course=? WHERE id=?",
              (name, surname, email, student_number, course, id))
        connection.commit()
        return True
    except sqlite3.Error as e:
        print("Error", e)
        return False
    finally:
        cursor.close()
        connection.close()

