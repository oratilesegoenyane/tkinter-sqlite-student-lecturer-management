import sqlite3



#delete the current student detail
def delete_student(id):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    connection.commit()
    connection.close()