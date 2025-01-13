import sqlite3


#delete the current lecture table
def delete_lecturer(id):
    connection = sqlite3.connect('lecturers.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM lecturers WHERE id=?", (id,))
    connection.commit()
    connection.close()