# 🗄️ Student Management System (MySQL + OOP Version)

A **menu-driven Student Management System** developed using **Python, MySQL, and Object-Oriented Programming (OOP)**.

This version is an enhanced implementation of the CSV-based application. Student records are stored in a **MySQL database**, and the application is organized using **classes and methods**, making the code cleaner, reusable, and easier to maintain.

---

## ✨ Features

- ➕ Add Student
- 📋 View Students
- 🔍 Search Student
- ✏️ Update Student
- ❌ Delete Student
- 🗄️ MySQL Database Integration
- 🏗️ Object-Oriented Programming (OOP)
- 🔒 Parameterized SQL Queries
- ✅ Input Validation
- ⚠️ Exception Handling
- 📜 Menu-Driven Interface

---

## 🛠️ Technologies Used

- Python
- MySQL
- mysql-connector-python
- Object-Oriented Programming (OOP)

---

## 📦 Installation

Install the required package:

```bash
pip install mysql-connector-python
```

---

## 🗄️ Database Setup

1. Create a MySQL database.

2. Create the `student` table:

```sql
CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL
);
```

3. Update your MySQL credentials inside the Python program:

```python
host="localhost"
user="root"
password="your_password"
database="gugan_db"
```

---

## ▶️ Run the Project

Navigate to the `mysql-version` folder and run:

```bash
python student_management_oop.py
```

---

## 📚 Learning Outcomes

Through this project, I learned:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Instance Variables and Methods
- CRUD Operations
- MySQL Database Connectivity
- SQL Queries
- Parameterized Queries
- Exception Handling
- Input Validation
- Code Refactoring
- Software Project Organization

---

## 📈 Improvements Over the CSV Version

- Migrated from CSV file storage to a MySQL database.
- Refactored the project using Object-Oriented Programming.
- Added database connectivity with `mysql-connector-python`.
- Reduced duplicate code by creating reusable helper methods.
- Improved error handling and input validation.
- Organized the application into a cleaner and more maintainable structure.

---

## 🔮 Future Improvements

- Develop a GUI using Tkinter or PyQt
- Build a web version using Flask or Django
- Add user authentication
- Export student records to Excel/PDF
- Add filtering and sorting features
- Implement role-based access control

---

## 👨‍💻 Author

**Gugan D**

GitHub: https://github.com/DGugan

---

⭐ If you found this project helpful, consider giving it a star!
