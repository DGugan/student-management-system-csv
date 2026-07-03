from getpass import getpass
from textwrap import dedent
import mysql.connector


class StudentManagement:

    def __init__(self):
        try:
            password = getpass("Enter MYSQL Password: ")
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password=password,
                database="gugan_db"
            )
            self.cursor = self.con.cursor()
            print("Database Connected Successfully!")
        except mysql.connector.Error as e:
            print("Connection Failed:", e)
            exit()

    def greeting(self):
        print("Welcome to Student Management System")

    def student_exists(self, student_id):
        query = "SELECT * FROM student WHERE student_id=%s"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchone()

    def add_student(self):
        print("========== ADDING STUDENTS ==========")

        name = input("Enter Student name: ")

        try:
            age = int(input("Enter Student age: "))
        except ValueError:
            print("Age must be a number.")
            return

        course = input("Enter Student course: ")

        query = "INSERT INTO student(name,age,course) VALUES(%s,%s,%s)"
        values = (name, age, course)

        self.cursor.execute(query, values)
        self.con.commit()

        print("Student added successfully.")

    def view_students(self):
        print("========== VIEW STUDENTS ==========")

        query = "SELECT * FROM student"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        if not rows:
            print("No students found")
            return

        for row in rows:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Course:", row[3])
            print("_" * 30)

    def search_student(self):
        print("========== SEARCH STUDENT ==========")

        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("Student ID must be a number.")
            return

        row = self.student_exists(student_id)

        if not row:
            print("Student not found")
            return

        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Course:", row[3])
        print("_" * 30)

    def update_student(self):

        print(dedent("""
        ========== UPDATE MENU ==========
        1. Update Name
        2. Update Age
        3. Update Course
        4. Back
        =================================
        """))

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Choice must be a number.")
            return

        if choice == 4:
            return

        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("Student ID must be a number.")
            return

        row = self.student_exists(student_id)

        if not row:
            print("Student not found")
            return

        if choice == 1:

            name = input("Enter new student name: ")

            query = "UPDATE student SET name=%s WHERE student_id=%s"
            self.cursor.execute(query, (name, student_id))
            self.con.commit()

            print("Student name updated successfully.")

        elif choice == 2:

            try:
                age = int(input("Enter new age: "))
            except ValueError:
                print("Age must be a number.")
                return

            query = "UPDATE student SET age=%s WHERE student_id=%s"
            self.cursor.execute(query, (age, student_id))
            self.con.commit()

            print("Student age updated successfully.")

        elif choice == 3:

            course = input("Enter new course: ")

            query = "UPDATE student SET course=%s WHERE student_id=%s"
            self.cursor.execute(query, (course, student_id))
            self.con.commit()

            print("Student course updated successfully.")

        else:
            print("Invalid choice.")

    def delete_student(self):

        print("========== DELETE STUDENT ==========")

        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("Student ID must be a number.")
            return

        row = self.student_exists(student_id)

        if not row:
            print("Student not found")
            return

        query = "DELETE FROM student WHERE student_id=%s"

        self.cursor.execute(query, (student_id,))
        self.con.commit()

        print("Student deleted successfully.")

    def menu(self):

        while True:

            print(dedent("""
            ========== MENU ==========
            1. Add Student
            2. Update Student
            3. Delete Student
            4. Search Student
            5. View Students
            6. Exit
            ==========================
            """))

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Choice must be an integer.")
                continue

            if choice == 1:
                self.add_student()

            elif choice == 2:
                self.update_student()

            elif choice == 3:
                self.delete_student()

            elif choice == 4:
                self.search_student()

            elif choice == 5:
                self.view_students()

            elif choice == 6:
                print("Thank you for using Student Management System.")
                self.con.close()
                break

            else:
                print("Invalid choice.")


sms = StudentManagement()
sms.greeting()
sms.menu()