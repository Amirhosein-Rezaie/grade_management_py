from database.Database import Database
from tools.func import table

# variables
student = Database("database.sqlite3")
columns = ["firstname", "lastname", "national_code"]


# add student
def add_student() -> int:
    "function add student to database"

    global student

    # get the information of student
    firstname = input("Enter the firstname of student : ")
    lastname = input("Enter the lastname of student : ")
    code = input("Enter the nationl code of student : ")

    # try to add the new student
    try:
        student.Get_Query(
            f"INSERT INTO students (firstname, lastname, code) VALUES ('{firstname}', '{lastname}', '{code}')"
        )

        print(f"Adding {firstname} {lastname} Successfully Done ... !", flush=True)

        return 0

    except:
        print("Adding new student Failed ... !", flush=True)

        return 1


# get all of students in the database
def show_all_students():
    "get all of students in the database"

    global student

    # get query to the database
    rows = student.Get_Query("SELECT * FROM students", fetch_result=True)

    # show the title or template of table of students
    table(rows, columns)


# delete a specific student by national code
def delete_student():
    "delete a specific student by national code"

    global student

    # get input from user
    code = input("Enter the national code of student that you want to delete : ")

    # try to found the student that is going to delete
    try:
        deleted_student = student.Get_Query(
            f"SELECT * FROM students WHERE code='{code}'", fetch_result=True
        )[0]
    except IndexError:
        print("The student not found ... !")

        return 1

    # try to delete the student by the nationl code
    try:
        student.Get_Query(f"DELETE FROM students WHERE code='{code}'")

        print(
            f"{deleted_student[1]} {deleted_student[2]} student deleted Successfully ... !"
        )

        return 0

    except:
        print(
            f"Deleting {deleted_student[1]} {deleted_student[2]} student failed ... !"
        )

        return 1


# edit the student data by using nationl code
def edit_student():
    "edit the student data by using nationl code"

    global student

    # get input natioal code from the user
    code = input("Enter the nationl code : ")

    # try to find the student that in going to edit
    data = None

    try:
        data = student.Get_Query(
            f"SELECT * FROM students WHERE code='{code}'", fetch_result=True
        )[0]
    except:
        print("The student not found ... !")
        return 1

    # show the data of student in a table
    table(data, columns)

    # get new data from the user
    new_firstname = input(f"Enter the new firstname of {data[1]} : ")
    new_lastname = input(f"Enter the new lastname of {data[2]} : ")
    new_code = input(f"Enter the new nationl_code of {data[3]} : ")

    # try to update data of the student in the database
    try:
        student.Get_Query(f"""UPDATE students 
                SET firstname='{new_firstname}', lastname='{new_lastname}', code='{new_code}'
                WHERE code='{code}'
                """)
        print("Student updated Successfuly ... !")

        return 0

    except:
        print("Updating student failed ... !")

        return 1


# search the student
def search_student() -> None:
    "search the student"

    code = input("Enter the national code : ")

    # try to find the student that in going to edit
    data = None

    try:
        data = student.Get_Query(
            f"SELECT * FROM students WHERE code='{code}'", fetch_result=True
        )
    except:
        print("The student not found ... !")
        return 1

    # show the data of student in a table
    table(data, columns)


# show average of one student
def average_student_in_subjects() -> None:
    "show average of one student"

    # get input national code of student
    code = input("Enter the national code of student : ")

    # get grades and show
    datas = []
    try:
        datas = student.Get_Query(
            f"""
            SELECT grades.id, students.firstname || ' ' || students.lastname, subjects.title DISTINC, grades.grade
            FROM students, grades, subjects
            WHERE (students.code={code}) AND students.id=grades.student_id AND subjects.id=grades.subject_id
            """,
            fetch_result=True,
        )
    except:
        print("Searching for student and the grades Failed ... !")
        return 0

    table(datas, ["student", "subject", "grade"], False)

    # calculate the average of grades
    try:
        grades = [data[3] for data in datas]

        print("The average of grades : " + str(sum(grades) / len(grades)))
        return 1

    except:
        print("Calculating of average the grades Failed ... !")
        return 0
