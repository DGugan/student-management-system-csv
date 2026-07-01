import csv
students=[]
def display_students():
    if len(students)==0:
        print("No students found")
        return
    for student in students:
        print(f"Name: ",student["name"])
        print(f"Age: ",student["age"])
        print(f"Course: ",student["course"])
        print("____________________________")

def student_exists(name):
    for student in students:
        if student['name']==name:
            return True
    return False
    

def add_students(name,age,course):
    student={
        "name":name,
        "age":age,
        "course":course
    }
    students.append(student)
    print("Student added successfully")


def search_student(name):
    for student in students:
        if student["name"] == name:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return
    print("Student Not Found")


def delete_students(name):
    for student in students:
        if student["name"]==name:
            students.remove(student)
            print("student deleted")
            save_students()
            return
    print("Student not found")

def count_students():
    if not students:
        print("No students available.")
        return

    print("Total Students:", len(students))

def update_students(name):
    for student in students:
        if student["name"]==name:
            new_age=int(input("Enter new age for the student:"))
            new_course=input("Enter new course for the student:")
            student["age"]=new_age
            student["course"]=new_course
            save_students()
            print("Student updated successfully.")
            return
        
    print("Student not found")

def save_students():
    with open("save_students.csv","w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["name","age","course"])
        for student in students:
            writer.writerow([
                student['name'],
                student['age'],
                student['course']
            ])
    print("Students saved successfully.")

def load_students():
    global students

    try:
        with open("save_students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "name": row["name"],
                    "age": int(row["age"]),
                    "course": row["course"]
                }

                students.append(student)

        print("Students loaded successfully.")

    except FileNotFoundError:
        print("No saved students found.")
load_students()
while True:
    print("----------MENU----------")
    print("1.Add Students")
    print("2.View Students")
    print("3.Search Students")
    print("4.Delete Students")
    print("5.Count studets")
    print("6.Update students")
    print("7.Exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Enter a Number")
        continue
    
    if choice==1:
        print("----------Add Students----------")
        name = input("Enter name: ")
        if student_exists(name):
            print("Student already exists")
            continue
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        add_students(name, age, course)
        save_students()
    elif choice==2:
        print("----------View Students----------")
        display_students()
    elif choice==3:        
        print("----------Search Students----------")
        name=input("Enter the student name to search:")
        search_student(name)
    elif choice==4:
        print("----------Delete Students----------")
        name=input("Enter the Student name to delete:")
        delete_students(name)
    elif choice==5:
        count_students()
    elif choice==6:
        name=input("Enter the student name to update:")
        update_students(name)
    elif choice==7:
        save_students()
        print("Exited")
        break
    else:
        print("invalid choice")