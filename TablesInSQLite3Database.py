#Creating tables in SQLite Database

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("BelgiumCampus.db")
cursor = conn.cursor()

# Create table for students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT,
                    student_number INTEGER UNIQUE,
                    course TEXT
                )''')

# Create table for lecturers
cursor.execute('''CREATE TABLE IF NOT EXISTS lecturers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    course TEXT,
                    department TEXT
                )''')

# Commit changes and close connection
conn.commit()
conn.close()
