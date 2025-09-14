import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import math

class StudentResultSystem:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Student Result Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Create database
        self.create_database()
        
        # Create main interface
        self.create_main_interface()
        
    def create_database(self):
        """Create database and tables"""
        try:
            conn = sqlite3.connect('student_results.db')
            cursor = conn.cursor()
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS students
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              roll_number TEXT UNIQUE NOT NULL,
                              class_name TEXT NOT NULL,
                              subject1 REAL,
                              subject2 REAL,
                              subject3 REAL,
                              subject4 REAL,
                              subject5 REAL,
                              total REAL,
                              percentage REAL,
                              grade TEXT,
                              status TEXT)''')
            
            conn.commit()
            conn.close()
            print("Database created successfully!")
            
        except Exception as e:
            messagebox.showerror("Database Error", f"Error creating database: {str(e)}")
    
    def create_main_interface(self):
        """Create the main interface with admin and student options"""
        # Title
        title_frame = Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=X)
        title_frame.pack_propagate(False)
        
        title_label = Label(title_frame, text="STUDENT RESULT MANAGEMENT SYSTEM", 
                           font=("Arial", 18, "bold"), fg="white", bg="#2c3e50")
        title_label.pack(pady=20)
        
        # Main content frame
        main_frame = Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=BOTH, padx=50, pady=50)
        
        # Welcome text
        welcome_label = Label(main_frame, text="Welcome to Student Result Management System", 
                             font=("Arial", 14), bg="#f0f0f0", fg="#2c3e50")
        welcome_label.pack(pady=20)
        
        # Buttons frame
        button_frame = Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        # Admin button
        admin_btn = Button(button_frame, text="ADMINISTRATOR LOGIN", 
                          font=("Arial", 12, "bold"), bg="#3498db", fg="white",
                          width=20, height=2, cursor="hand2",
                          command=self.admin_login)
        admin_btn.pack(pady=10)
        
        # Student button
        student_btn = Button(button_frame, text="STUDENT LOGIN", 
                           font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                           width=20, height=2, cursor="hand2",
                           command=self.student_login)
        student_btn.pack(pady=10)
        
        # Exit button
        exit_btn = Button(button_frame, text="EXIT", 
                         font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                         width=20, height=2, cursor="hand2",
                         command=self.root.quit)
        exit_btn.pack(pady=10)
        
    def admin_login(self):
        """Admin login window"""
        login_window = Toplevel(self.root)
        login_window.title("Administrator Login")
        login_window.geometry("400x300")
        login_window.configure(bg="#f0f0f0")
        login_window.grab_set()
        
        # Title
        Label(login_window, text="Administrator Login", font=("Arial", 16, "bold"), 
              bg="#f0f0f0", fg="#2c3e50").pack(pady=20)
        
        # Username
        Label(login_window, text="Username:", font=("Arial", 12), 
              bg="#f0f0f0").pack(pady=5)
        username_entry = Entry(login_window, font=("Arial", 12), width=20)
        username_entry.pack(pady=5)
        
        # Password
        Label(login_window, text="Password:", font=("Arial", 12), 
              bg="#f0f0f0").pack(pady=5)
        password_entry = Entry(login_window, font=("Arial", 12), width=20, show="*")
        password_entry.pack(pady=5)
        
        def verify_admin():
            if username_entry.get() == "admin" and password_entry.get() == "admin123":
                login_window.destroy()
                self.admin_panel()
            else:
                messagebox.showerror("Error", "Invalid credentials!\nUsername: admin\nPassword: admin123")
        
        # Login button
        Button(login_window, text="LOGIN", font=("Arial", 12, "bold"), 
               bg="#3498db", fg="white", command=verify_admin).pack(pady=20)
        
        # Default credentials info
        Label(login_window, text="Default: Username: admin, Password: admin123", 
              font=("Arial", 10), bg="#f0f0f0", fg="#7f8c8d").pack(pady=10)
    
    def admin_panel(self):
        """Administrator panel window"""
        admin_window = Toplevel(self.root)
        admin_window.title("Administrator Panel")
        admin_window.geometry("900x700")
        admin_window.configure(bg="#f0f0f0")
        admin_window.grab_set()
        
        # Title
        Label(admin_window, text="Administrator Panel", font=("Arial", 18, "bold"), 
              bg="#f0f0f0", fg="#2c3e50").pack(pady=10)
        
        # Notebook for tabs
        notebook = ttk.Notebook(admin_window)
        notebook.pack(expand=True, fill=BOTH, padx=20, pady=20)
        
        # Add Student Tab
        add_frame = Frame(notebook, bg="#f0f0f0")
        notebook.add(add_frame, text="Add Student")
        
        # View Students Tab
        view_frame = Frame(notebook, bg="#f0f0f0")
        notebook.add(view_frame, text="View Students")
        
        self.create_add_student_tab(add_frame)
        self.create_view_student_tab(view_frame)
    
    def create_add_student_tab(self, parent):
        """Create add student tab interface"""
        # Title
        Label(parent, text="Add New Student Record", font=("Arial", 16, "bold"), 
              bg="#f0f0f0", fg="#2c3e50").pack(pady=20)
        
        # Form frame
        form_frame = Frame(parent, bg="#f0f0f0")
        form_frame.pack(pady=20)
        
        # Student details
        Label(form_frame, text="Student Name:", font=("Arial", 12), 
              bg="#f0f0f0").grid(row=0, column=0, sticky=W, padx=10, pady=5)
        name_entry = Entry(form_frame, font=("Arial", 12), width=25)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        Label(form_frame, text="Roll Number:", font=("Arial", 12), 
              bg="#f0f0f0").grid(row=1, column=0, sticky=W, padx=10, pady=5)
        roll_entry = Entry(form_frame, font=("Arial", 12), width=25)
        roll_entry.grid(row=1, column=1, padx=10, pady=5)
        
        Label(form_frame, text="Class:", font=("Arial", 12), 
              bg="#f0f0f0").grid(row=2, column=0, sticky=W, padx=10, pady=5)
        class_entry = Entry(form_frame, font=("Arial", 12), width=25)
        class_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Subject marks
        subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
        mark_entries = []
        
        Label(form_frame, text="Subject Marks:", font=("Arial", 12, "bold"), 
              bg="#f0f0f0").grid(row=3, column=0, columnspan=2, pady=10)
        
        for i, subject in enumerate(subjects):
            Label(form_frame, text=f"{subject}:", font=("Arial", 11), 
                  bg="#f0f0f0").grid(row=4+i, column=0, sticky=W, padx=10, pady=3)
            entry = Entry(form_frame, font=("Arial", 11), width=10)
            entry.grid(row=4+i, column=1, sticky=W, padx=10, pady=3)
            mark_entries.append(entry)
        
        def add_student():
            try:
                name = name_entry.get().strip()
                roll = roll_entry.get().strip()
                class_name = class_entry.get().strip()
                
                if not name or not roll or not class_name:
                    messagebox.showerror("Error", "Please fill all required fields!")
                    return
                
                marks = []
                for entry in mark_entries:
                    mark = entry.get().strip()
                    if mark:
                        mark_val = float(mark)
                        if mark_val < 0 or mark_val > 100:
                            messagebox.showerror("Error", "Marks should be between 0 and 100!")
                            return
                        marks.append(mark_val)
                    else:
                        marks.append(0.0)
                
                # Calculate total, percentage and grade
                total = sum(marks)
                percentage = total / 5
                
                if percentage >= 90:
                    grade = "A+"
                    status = "PASS"
                elif percentage >= 80:
                    grade = "A"
                    status = "PASS"
                elif percentage >= 70:
                    grade = "B+"
                    status = "PASS"
                elif percentage >= 60:
                    grade = "B"
                    status = "PASS"
                elif percentage >= 50:
                    grade = "C"
                    status = "PASS"
                elif percentage >= 40:
                    grade = "D"
                    status = "PASS"
                else:
                    grade = "F"
                    status = "FAIL"
                
                # Insert into database
                conn = sqlite3.connect('student_results.db')
                cursor = conn.cursor()
                
                cursor.execute('''INSERT INTO students 
                                 (name, roll_number, class_name, subject1, subject2, subject3, subject4, subject5, total, percentage, grade, status)
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                              (name, roll, class_name, marks[0], marks[1], marks[2], marks[3], marks[4], total, percentage, grade, status))
                
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Success", f"Student {name} added successfully!\nTotal: {total}\nPercentage: {percentage:.2f}%\nGrade: {grade}")
                
                # Clear entries
                name_entry.delete(0, END)
                roll_entry.delete(0, END)
                class_entry.delete(0, END)
                for entry in mark_entries:
                    entry.delete(0, END)
                    
            except ValueError:
                messagebox.showerror("Error", "Please enter valid marks (numbers only)!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Roll number already exists!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        # Add button
        Button(form_frame, text="ADD STUDENT", font=("Arial", 12, "bold"), 
               bg="#27ae60", fg="white", command=add_student).grid(row=10, column=0, columnspan=2, pady=20)
    
    def create_view_student_tab(self, parent):
        """Create view students tab interface"""
        # Title
        Label(parent, text="View Student Records", font=("Arial", 16, "bold"), 
              bg="#f0f0f0", fg="#2c3e50").pack(pady=10)
        
        # Search frame
        search_frame = Frame(parent, bg="#f0f0f0")
        search_frame.pack(pady=10)
        
        Label(search_frame, text="Search by Roll Number:", font=("Arial", 12), 
              bg="#f0f0f0").pack(side=LEFT, padx=5)
        search_entry = Entry(search_frame, font=("Arial", 12), width=15)
        search_entry.pack(side=LEFT, padx=5)
        
        # Treeview for displaying records
        tree_frame = Frame(parent, bg="#f0f0f0")
        tree_frame.pack(expand=True, fill=BOTH, padx=20, pady=10)
        
        # Scrollbar
        scrollbar = Scrollbar(tree_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Treeview
        tree = ttk.Treeview(tree_frame, yscrollcommand=scrollbar.set)
        tree['columns'] = ('Name', 'Roll', 'Class', 'Total', 'Percentage', 'Grade', 'Status')
        tree.column('#0', width=0, stretch=NO)
        tree.column('Name', width=150)
        tree.column('Roll', width=100)
        tree.column('Class', width=100)
        tree.column('Total', width=80)
        tree.column('Percentage', width=100)
        tree.column('Grade', width=80)
        tree.column('Status', width=80)
        
        tree.heading('Name', text='Name')
        tree.heading('Roll', text='Roll No')
        tree.heading('Class', text='Class')
        tree.heading('Total', text='Total')
        tree.heading('Percentage', text='Percentage')
        tree.heading('Grade', text='Grade')
        tree.heading('Status', text='Status')
        
        tree.pack(expand=True, fill=BOTH)
        scrollbar.config(command=tree.yview)
        
        def load_all_students():
            # Clear existing records
            for item in tree.get_children():
                tree.delete(item)
            
            try:
                conn = sqlite3.connect('student_results.db')
                cursor = conn.cursor()
                cursor.execute("SELECT name, roll_number, class_name, total, percentage, grade, status FROM students")
                records = cursor.fetchall()
                
                for record in records:
                    tree.insert('', 'end', values=record)
                
                conn.close()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error loading data: {str(e)}")
        
        def search_student():
            search_term = search_entry.get().strip()
            if not search_term:
                load_all_students()
                return
            
            # Clear existing records
            for item in tree.get_children():
                tree.delete(item)
            
            try:
                conn = sqlite3.connect('student_results.db')
                cursor = conn.cursor()
                cursor.execute("SELECT name, roll_number, class_name, total, percentage, grade, status FROM students WHERE roll_number LIKE ?", 
                              (f'%{search_term}%',))
                records = cursor.fetchall()
                
                for record in records:
                    tree.insert('', 'end', values=record)
                
                if not records:
                    messagebox.showinfo("No Results", "No student found with that roll number!")
                
                conn.close()
                
            except Exception as e:
                messagebox.showerror("Error", f"Error searching: {str(e)}")
        
        # Buttons
        button_frame = Frame(parent, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        Button(button_frame, text="SEARCH", font=("Arial", 10, "bold"), 
               bg="#f39c12", fg="white", command=search_student).pack(side=LEFT, padx=5)
        
        Button(button_frame, text="LOAD ALL", font=("Arial", 10, "bold"), 
               bg="#9b59b6", fg="white", command=load_all_students).pack(side=LEFT, padx=5)
        
        # Load all students initially
        load_all_students()
    
    def student_login(self):
        """Student login window"""
        student_window = Toplevel(self.root)
        student_window.title("Student Login")
        student_window.geometry("500x400")
        student_window.configure(bg="#f0f0f0")
        student_window.grab_set()
        
        # Title
        Label(student_window, text="Student Result Portal", font=("Arial", 16, "bold"), 
              bg="#f0f0f0", fg="#2c3e50").pack(pady=20)
        
        # Roll number entry
        Label(student_window, text="Enter Your Roll Number:", font=("Arial", 12), 
              bg="#f0f0f0").pack(pady=10)
        roll_entry = Entry(student_window, font=("Arial", 14), width=20)
        roll_entry.pack(pady=10)
        
        # Result display frame
        result_frame = Frame(student_window, bg="#f0f0f0")
        result_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)
        
        def show_result():
            roll_number = roll_entry.get().strip()
            if not roll_number:
                messagebox.showerror("Error", "Please enter your roll number!")
                return
            
            try:
                conn = sqlite3.connect('student_results.db')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
                student = cursor.fetchone()
                conn.close()
                
                # Clear previous results
                for widget in result_frame.winfo_children():
                    widget.destroy()
                
                if student:
                    # Display result card
                    card_frame = Frame(result_frame, bg="white", relief=RIDGE, bd=2)
                    card_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)
                    
                    Label(card_frame, text="STUDENT RESULT CARD", font=("Arial", 16, "bold"), 
                          bg="white", fg="#2c3e50").pack(pady=10)
                    
                    # Student info
                    info_frame = Frame(card_frame, bg="white")
                    info_frame.pack(pady=10)
                    
                    Label(info_frame, text=f"Name: {student[1]}", font=("Arial", 12), 
                          bg="white").pack(anchor=W, padx=20)
                    Label(info_frame, text=f"Roll Number: {student[2]}", font=("Arial", 12), 
                          bg="white").pack(anchor=W, padx=20)
                    Label(info_frame, text=f"Class: {student[3]}", font=("Arial", 12), 
                          bg="white").pack(anchor=W, padx=20)
                    
                    # Marks table
                    marks_frame = Frame(card_frame, bg="white")
                    marks_frame.pack(pady=20)
                    
                    subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
                    marks = [student[4], student[5], student[6], student[7], student[8]]
                    
                    Label(marks_frame, text="SUBJECT WISE MARKS", font=("Arial", 14, "bold"), 
                          bg="white").pack(pady=10)
                    
                    for i, (subject, mark) in enumerate(zip(subjects, marks)):
                        Label(marks_frame, text=f"{subject}: {mark}/100", font=("Arial", 11), 
                              bg="white").pack(anchor=W, padx=20)
                    
                    # Summary
                    summary_frame = Frame(card_frame, bg="white")
                    summary_frame.pack(pady=20)
                    
                    Label(summary_frame, text=f"Total Marks: {student[9]}/500", font=("Arial", 12, "bold"), 
                          bg="white", fg="#2c3e50").pack()
                    Label(summary_frame, text=f"Percentage: {student[10]:.2f}%", font=("Arial", 12, "bold"), 
                          bg="white", fg="#2c3e50").pack()
                    Label(summary_frame, text=f"Grade: {student[11]}", font=("Arial", 14, "bold"), 
                          bg="white", fg="#e74c3c" if student[12] == "FAIL" else "#27ae60").pack()
                    Label(summary_frame, text=f"Status: {student[12]}", font=("Arial", 14, "bold"), 
                          bg="white", fg="#e74c3c" if student[12] == "FAIL" else "#27ae60").pack()
                    
                else:
                    Label(result_frame, text="No record found for this roll number!", 
                          font=("Arial", 14), bg="#f0f0f0", fg="#e74c3c").pack(pady=50)
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error retrieving result: {str(e)}")
        
        # Search button
        Button(student_window, text="GET RESULT", font=("Arial", 12, "bold"), 
               bg="#27ae60", fg="white", command=show_result).pack(pady=10)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# Sample data insertion function (for testing)
def insert_sample_data():
    """Insert some sample student data for testing"""
    try:
        conn = sqlite3.connect('student_results.db')
        cursor = conn.cursor()
        
        sample_students = [
            ("John Doe", "2024001", "10th Grade", 85, 78, 92, 88, 90, 433, 86.6, "A", "PASS"),
            ("Jane Smith", "2024002", "10th Grade", 95, 89, 94, 91, 96, 465, 93.0, "A+", "PASS"),
            ("Bob Johnson", "2024003", "10th Grade", 45, 38, 42, 48, 35, 208, 41.6, "D", "PASS"),
            ("Alice Brown", "2024004", "10th Grade", 25, 30, 28, 35, 32, 150, 30.0, "F", "FAIL"),
        ]
        
        for student in sample_students:
            cursor.execute('''INSERT OR REPLACE INTO students 
                             (name, roll_number, class_name, subject1, subject2, subject3, subject4, subject5, total, percentage, grade, status)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', student)
        
        conn.commit()
        conn.close()
        print("Sample data inserted successfully!")
        
    except Exception as e:
        print(f"Error inserting sample data: {str(e)}")

if _name_ == "_main_":
    # Insert sample data (comment this line after first run)
    insert_sample_data()
    
    # Create and run the application
    app = StudentResultSystem()
    app.run()
