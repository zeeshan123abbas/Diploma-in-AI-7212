# crud_mysql.py
# Create, Read, Update, Delete (CRUD) with MySQL from Python
import mysql.connector
from db_config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def add_student(name, city, marks):
    conn = get_connection()
    cursor = conn.cursor()
    # %s placeholders keep the query safe from SQL injection
    sql = "INSERT INTO students (name, city, marks) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, city, marks))
    conn.commit()                      # save the change
    print("Inserted id:", cursor.lastrowid)
    conn.close()

def show_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)   # rows as dictionaries
    cursor.execute("SELECT id, name, city, marks FROM students ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_marks(student_id, new_marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (new_marks, student_id))
    conn.commit()
    print("Rows updated:", cursor.rowcount)
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    print("Rows deleted:", cursor.rowcount)
    conn.close()

if __name__ == "__main__":
    add_student("Hina", "Islamabad", 85)
    show_students()
    update_marks(1, 82)
    delete_student(3)
    show_students()
