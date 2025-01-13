import sqlite3


#select the current lecture detail
def retrieve_lecturers():
    try:
            connection = sqlite3.connect('lecturers.db')
            cursor = connection.cursor()
            # fetch all data from table in SQL db
            cursor.execute("SELECT * FROM lecturers")
            # store all fetched data inside results variable
            lecturers = cursor.fetchall()
            print("Lecturers retrieved successfully.")
            return lecturers

    except sqlite3.Error as e:
            print("Error", e)
            return None

    finally:
            cursor.close()
            connection.close()

lecturers = retrieve_lecturers()
if lecturers:
    for lecturer in lecturers:
        print(lecturer)
else:
        print("No lecturers found.")