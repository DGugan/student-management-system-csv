import mysql.connector
from getpass import getpass

def add_student():
    print("========== ADDING STUDENTS ==========")
    name=input("Enter Student name:")
    try:
        age=int(input("Enter Student age:"))
    except ValueError:
        print("Age must be a number.")
        return
    course=input("Enter Student course:")
    query="INSERT INTO student(name,age,course) VALUES(%s,%s,%s)"
    value=(name,age,course,)
    cursor.execute(query,value)
    con.commit()
    print("Student added successfully.")

def view_students():
    print("========== VIEW STUDENTS ==========")
    query="SELECT * FROM student"
    cursor.execute(query)
    rows=cursor.fetchall()
    if not rows:
        print("No students found")
        return
    for row in rows:
        print("ID:",row[0])
        print("Name:",row[1])
        print("Age:",row[2])
        print("Course:",row[3])
        print("_" * 30)


def search_student():
    print("========== SEARCH STUDENT ==========")
    try:
        student_id = int(input("Enter student id: "))
    except ValueError:
        print("Student ID must be a number.")
        return
    query="SELECT * FROM student WHERE student_id=%s"
    value=(student_id,)
    cursor.execute(query,value)
    rows=cursor.fetchone()
    if not rows :
        print("No students found")
        return
    print("ID:",rows[0])
    print("Name:",rows[1])
    print("Age:",rows[2])
    print("Course:",rows[3])
    print("_" * 30)

def update_student():
    print("""========== UPDATE MENU ==========
          1. Update Name
          2. Update Age
          3. Update Course
          4. Back
          =================================""")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("========== UPDATE NAME ==========")
        try:
            student_id=int(input("Enter student id to make update:"))
        except ValueError:
            print("Student ID must be a number.")
            return
        check_query="SELECT * FROM student WHERE student_id=%s"
        values=(student_id,)
        cursor.execute(check_query,values)
        row=cursor.fetchone()
        if not row:
            print("Student not found")
        else:
            name=input("Enter student name to update: ")
            query="UPDATE student SET name=%s WHERE student_id=%s"
            value=(name,student_id,)
            cursor.execute(query,value)
            if cursor.rowcount>0:
                con.commit()
                print("Student name updated successfully.")
            else:
                print("Student not found")


    elif choice==2:
        print("========== UPDATE AGE ==========")
        try:
            student_id=int(input("Enter student id to make update:"))
        except ValueError:
            print("Student ID must be a number.")
            return
        check_query="SELECT * FROM student WHERE student_id=%s"
        values=(student_id,)
        cursor.execute(check_query,values)
        row=cursor.fetchone()
        if not row:
            print("Student not found")
        else:
            try:
                age = int(input("Enter student age to update: "))
            except ValueError:
                print("Age must be a number.")
                return
            query="UPDATE student SET age=%s WHERE student_id=%s"
            value=(age,student_id,)
            cursor.execute(query,value)
            if cursor.rowcount>0:
                con.commit()
                print("Student age updated successfully.")
            else:
                print("Student not found")
    elif choice==3:
        print("========== UPDATE COURSE ==========")
        try:
            student_id=int(input("Enter student id to make update:"))
        except ValueError:
            print("Student ID must be a number.")
            return
        check_query="SELECT * FROM student WHERE student_id=%s"
        values=(student_id,)
        cursor.execute(check_query,values)
        row=cursor.fetchone()
        if not row:
            print("Student not found")
        else:
            course=input("Enter student course to update: ")
            query="UPDATE student SET course=%s WHERE student_id=%s"
            value=(course,student_id,)
            cursor.execute(query,value)
            if cursor.rowcount>0:
                con.commit()
                print("Student course updated successfully.")
            else:
                print("Student not found")
    elif choice==4:
        print("Returning To Main Menu")
        return
    
def delete_student():
    print("========== DELETE STUDENTS ==========")
    try:
        student_id=int(input("Enter student id to delete:"))
    except ValueError:
        print("Student ID must be a number.")
        return
    
    check_query="SELECT * FROM student WHERE student_id=%s"
    values=(student_id,)
    cursor.execute(check_query,values)
    row=cursor.fetchone()
    if not row:
        print("Student not found")
    else:
        query="DELETE FROM student WHERE student_id=%s"
        cursor.execute(query,values)
        con.commit()
        print("Student deleted successfully.")



password=getpass("Enter Your password: ")
try:
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="gugan_db"
    )
    cursor=con.cursor()

    while True:
        print("""
        ========== MENU ==========
        1. Add Student
        2. View Students
        3. Search Student
        4. Update Student
        5. Delete Student
        6. Exit
        ==========================""")
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                add_student()
            elif choice==2:
                view_students()
            elif choice==3:
                search_student()
            elif choice==4:
                update_student()
            elif choice==5:
                delete_student()
            elif choice==6:
                print("=====Exiting======")
                con.close()
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter valid choice")
except mysql.connector.Error as e:
    print("ERROR:",e)