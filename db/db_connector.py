import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import random

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="quiz_app"
    )

def get_random_questions(subject, level, num_questions):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    print("~~~~~~~~~~~~~~~",subject,level, num_questions)
    # Query to get random questions based on subject and level
    query = f"""
    SELECT id, question_text, option_a, option_b, option_c, option_d, correct_option 
    FROM questions 
    WHERE subject = %s AND level = %s 
    ORDER BY RAND() 
    LIMIT %s;
    """
    cursor.execute(query, (subject, level, num_questions))
    questions = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return questions

def save_quiz_response(student_id, question_id, selected_option):
    """
    Save the student’s selected option for a given question in the database.
    """
    db = connect_db()
    cursor = db.cursor()

    # Query to insert the student's response
    query = """
    INSERT INTO responses (student_id, question_id, selected_option)
    VALUES (%s, %s, %s)
    """
    
    cursor.execute(query, (student_id, question_id, selected_option))
    db.commit()
    db.close()

def check_login(registration_no, password):
    """
    Validate student login using registration number and password.
    """
    try:
        # Connect to the database
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        # Define the query to check the student's credentials
        query = """
        SELECT id, name, class
        FROM students
        WHERE regno = %s AND password = %s
        """

        print("Calling DB to validate login...")
        cursor.execute(query, (registration_no, password))

        # Fetch the student's record
        student = cursor.fetchone()

        # Close the database connection
        db.close()

        # Check if a student record was found
        if student is None:
            print("Login failed: Invalid registration number or password.")
            return None  # Return None if credentials are invalid
        
        print(f"Login successful: Student {student['name']} found.")
        return student  # Return the student information if login is valid
    
    except Exception as e:
        print(f"Error occurred while checking login: {e}")
        return None  # Return None in case of any error



def register_student(regno, name, house, stdclass,password):
    """
    Register a new student with name, class, registration number, and password.
    """
    db = connect_db()
    cursor = db.cursor()

    # Check if the registration number is already used
    check_query = "SELECT COUNT(*) FROM students WHERE regno = %s"
    cursor.execute(check_query, (regno,))
    (exists,) = cursor.fetchone()

    if exists:
        db.close()
        return False  # Registration number is already taken

    # Register the new student
    insert_query = """
    INSERT INTO students (regno, name, house, class,password)
    VALUES (%s, %s, %s, %s,%s)
    """
    cursor.execute(insert_query, (regno, name, house, stdclass,password))
    db.commit()
    db.close()

    return True  # Registration was successful

def get_subjects():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT  subject_name FROM quiz_subject")
    subjects = [row[0] for row in cursor.fetchall()]
    db.close()
    return subjects

def fetch_quiz_history(student_id):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    query = """
        SELECT q.question_text, q.option_a, q.option_b, q.option_c, q.option_d,
               qs.selected_option, q.correct_option, qs.exam_date
        FROM quiz_sessions qs
        JOIN questions q ON qs.question_id = q.id
        WHERE qs.student_id = %s
        ORDER BY qs.exam_date DESC
    """
    cursor.execute(query, (student_id,))
    history = cursor.fetchall()
    db.close()
    return history