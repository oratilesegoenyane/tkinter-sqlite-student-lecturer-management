import sqlite3

#inserting values in students table
def insert_students(name, surname, email, student_number, course):
    try:

            connection = sqlite3.connect("students.db")
            cursor = connection.cursor()

        # Execute an SQL INSERT statement
            cursor.execute("INSERT INTO students (name, surname, email, student_number, course) VALUES (?, ?, ?, ?, ?)",(name, surname, email, student_number, course))

        # Commit the transaction
            connection.commit()
            print("Student inserted successfully.")

    except sqlite3.Error as e:
             print("Error:", e)

    finally:
       # Close the cursor and the connection
       cursor.close()
       connection.close()

