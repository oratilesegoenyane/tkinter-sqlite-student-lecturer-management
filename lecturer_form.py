import tkinter as tk
from tkinter import messagebox, Listbox, ttk
import lecturer_create as lc
import lecturer_insert as li
import lecturer_update as lu
import lecturer_read as lr
import lecturer_delete as ld


class LecturerForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Lecturer Form")
        self.geometry("700x500")
        self.config(bg="#333333")


        welcome_label = ttk.Label(self, text="Lecturer Details", font=("Arial", 24, "bold"), foreground="white",
                                  background="#333333")
        welcome_label.pack()


#Define StringVar variables for input fields
        self.name_var = tk.StringVar()
        self.surname_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.department_var = tk.StringVar()

#Create a frame to hold the widgets
        self.frame = tk.Frame(self, bg="#D3D3D3")
        self.frame.pack(expand=True, fill=tk.BOTH)

#Labels and Entry widgets for lecture details
        tk.Label(self.frame, text="Lecturer Name:", font = ('bold', 14)).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.frame, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Lecturer Surname:", font = ('bold', 14)).grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.frame, textvariable=self.surname_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Course:", font = ('bold', 14)).grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.frame, textvariable=self.course_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.frame, text="Department:", font = ('bold', 14)).grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(self.frame, textvariable=self.department_var).grid(row=3, column=1, padx=10, pady=5)

#Listbox to display lecture details
        self.listbox = Listbox(self.frame, width=70, height=10)
        self.listbox.grid(row=4, columnspan=2, padx=10, pady=5)



#Load existing students
        self.load_lecturers()

#Buttons for CRUD operations
        add_btn = tk.Button(self.frame, text="Add", font = 'bold', command=self.add_lecturer,foreground="white", background="black")
        add_btn.grid(row=5, column=0, padx=10, pady=5)

        update_btn = tk.Button(self.frame, text="Update", font = 'bold', command=self.update_lecturer,foreground="white", background="black")
        update_btn.grid(row=5, column=1, padx=10, pady=5)

        delete_btn = tk.Button(self.frame, text="Delete", font = 'bold', command=self.delete_lecturer, foreground="white", background="black")
        delete_btn.grid(row=6, column=0, padx=10, pady=5)

        clear_btn = tk.Button(self.frame, text="Clear", font = 'bold', command=self.clear_lecturer_listbox,foreground="white", background="black")
        clear_btn.grid(row=6, column=1, padx=10, pady=5)



    def clear_lecturer_listbox(self):
        # Delete all items from the listbox
        self.listbox.delete(0, tk.END)

    def add_lecturer(self):
        name = self.name_var.get()
        surname = self.surname_var.get()
        course = self.course_var.get()
        department = self.department_var.get()

        if name and surname and course and department:
            li.insert_lecturer(name, surname, course, department)
            self.listbox.insert(tk.END, f"{name} {surname}, {course}, {department}")
            self.clear_fields()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def load_lecturers(self):
        lecturers = lr.retrieve_lecturers()
        for lecturer in lecturers:
            self.listbox.insert(tk.END, f"{lecturer[1]} {lecturer[2]}, {lecturer[3]}, {lecturer[4]}")

    def update_lecturer(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_lecturer = self.listbox.get(selected_index)
            parts = selected_lecturer.split(" - ")
            id = parts[-1]
            name = self.name_var.get()
            surname = self.surname_var.get()
            course = self.course_var.get()
            department = self.department_var.get()

            if name and surname and course and department:
                lu.update_lecturer(id, name, surname, course, department)
                self.listbox.delete(selected_index)
                self.listbox.insert(selected_index, f"{name} {surname}, {course}, {department}")
                self.clear_fields()
            else:
                messagebox.showwarning("Warning", "Please fill in all fields.")
        else:
            messagebox.showwarning("Warning", "Please select a lecturer to update.")

    def delete_lecturer(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_lecturer = self.listbox.get(selected_index)
            parts = selected_lecturer.split(", ")
            id = parts[-1]
            ld.delete_lecturer(id)
            self.listbox.delete(selected_index)
            self.clear_fields()
        else:
            messagebox.showwarning("Warning", "Please select a lecturer to delete.")

    def clear_fields(self):
        self.name_var.set("")
        self.surname_var.set("")
        self.course_var.set("")
        self.department_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = LecturerForm(root)
    root.mainloop()




