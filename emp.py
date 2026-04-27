import sqlite3

DB_NAME = "employee.db"


# ─────────────────────────────────────────────
# Connection
# ─────────────────────────────────────────────
def connect():
    return sqlite3.connect(DB_NAME)


# ─────────────────────────────────────────────
# Create Table
# ─────────────────────────────────────────────
def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        gender TEXT,
        department TEXT,
        salary INTEGER,
        city TEXT,
        joining_date TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# Insert Employee
# ─────────────────────────────────────────────
def add_employee(first_name, last_name, age, gender,
                 department, salary, city, joining_date, email):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees 
    (first_name, last_name, age, gender, department, salary, city, joining_date, email)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, age, gender,
          department, salary, city, joining_date, email))

    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# Fetch All Employees
# ─────────────────────────────────────────────
def fetch_employees():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    conn.close()
    return rows


# ─────────────────────────────────────────────
# Delete Employee
# ─────────────────────────────────────────────
def delete_employee(emp_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))

    conn.commit()
    conn.close()


# ─────────────────────────────────────────────
# Update Employee
# ─────────────────────────────────────────────
def update_employee(emp_id, first_name, last_name, age, gender,
                    department, salary, city, joining_date, email):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees
    SET first_name=?, last_name=?, age=?, gender=?,
        department=?, salary=?, city=?, joining_date=?, email=?
    WHERE emp_id=?
    """, (first_name, last_name, age, gender,
          department, salary, city, joining_date, email, emp_id))

    conn.commit()
    conn.close()