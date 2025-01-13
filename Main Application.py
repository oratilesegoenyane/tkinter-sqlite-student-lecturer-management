import tkinter
# main.py
import tkinter as tk
from tkinter import ttk
from student_form import StudentForm
from lecturer_form import LecturerForm

def animate_label(label, color1, color2,color3, delay):
    """Animate label color alternation."""
    label.config(foreground=color1)
    label.after(delay, lambda: animate_label(label, color3, color2, color1, delay))

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BC Management System")
        self.geometry("500x300")
        self.config(background="#333333") #ADD8E6
 

        # Display a welcome title with bold text
        welcome_label = ttk.Label(self, text="Welcome to Belgium Campus Student & Lecturer Management System", font=("Arial", 24, "bold"), foreground="white",
                                  background="#333333") #f7f8fa
        welcome_label.pack()


        self.student_form = None
        self.lecturer_form = None

        self.frame = tk.Frame(self, bg="#D3D3D3")
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.btn_student = tk.Button(self.frame, text="Student Management System", font = ('bold', 14), command=self.open_student_form, bg="#1E1E1E", padx=10, pady=5)
        self.btn_student.pack(pady=10)
        animate_label(self.btn_student, "red", "black", "yellow", 1000)

        self.btn_lecturer = tk.Button(self.frame, text="Lecturer Management System", font = ('bold', 14), command=self.open_lecturer_form, bg="#1E1E1E", padx=10, pady=5)
        self.btn_lecturer.pack(pady=10)
        animate_label(self.btn_lecturer, "yellow", "black", "red", 1000)

    def open_student_form(self):
        if not self.student_form:
            self.student_form = StudentForm(self)
            self.student_form.protocol("WM_DELETE_WINDOW", self.close_student_form)
            self.student_form.grab_set()

    def close_student_form(self):
        self.student_form.destroy()
        self.student_form = None

    def open_lecturer_form(self):
        if not self.lecturer_form:
            self.lecturer_form = LecturerForm(self)
            self.lecturer_form.protocol("WM_DELETE_WINDOW", self.close_lecturer_form)
            self.lecturer_form.grab_set()

    def close_lecturer_form(self):
        self.lecturer_form.destroy()
        self.lecturer_form = None

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
















