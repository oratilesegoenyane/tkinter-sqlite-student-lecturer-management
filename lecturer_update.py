import sqlite3

#update the current lecture table
def update_lecturer(id, name, surname, course, department):
    try:
        connection = sqlite3.connect('lecturers.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE lecturers SET name=?, surname=?, course=?, department=? WHERE id=?",
                               (name, surname, course, department, id))
        connection.commit()
        return True
    except sqlite3.Error as e:
           print("Error", e)
           return False
    finally:
            cursor.close()
            connection.close()

