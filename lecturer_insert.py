import sqlite3

#inserting values in lecturer table
def insert_lecturer(name, surname, course, department):
        try:
            # Open a connection to the SQLite database
            connection = sqlite3.connect("lecturers.db")
            cursor = connection.cursor()

            # Execute an SQL INSERT statement
            cursor.execute("INSERT INTO lecturers (name, surname, course, department) VALUES (?, ?, ?, ?)",
                           (name, surname, course, department))

            # Commit the transaction
            connection.commit()
            print("Lecturer inserted successfully.")

        except sqlite3.Error as e:
            print("Error:", e)

        finally:
            # Close the cursor and the connection
            cursor.close()
            connection.close()

