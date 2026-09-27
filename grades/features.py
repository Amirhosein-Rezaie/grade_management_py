from database.Database import Database
from grades.tools import search_one_record, TABLE_SBJ, TABLE_STD, check_grade
from subjects.features import search_subject
from tools.func import table, check_number_greater_zero

# variables
grade = Database("database.sqlite3")
COLUMNS = ["grade", "student", "subject"]


# # function
# add a grade
def add_grade() -> None:
    "add a grade"

    # variables
    global grade

    student_id = 0
    student_name = ""

    subject_id = 0
    subject_title = ""

    # get ID of the student
    while True:
        student_code = input("Enter the national code of student : ")
        data = search_one_record(student_code, TABLE_STD)

        if data == False:
            print("The student not found ... !")
        else:
            student_id = data[0]
            student_name = data[1] + " " + data[2]
            break

    # get code of the subject
    while True:
        find_sbj_search = search_subject()

        if find_sbj_search == 0:
            break

    # get ID of the subject
    while True:
        subject_code = input("Enter the code of subject : ")

        data = search_one_record(subject_code, TABLE_SBJ)

        if data == False:
            print("The subject not found ... !")
        else:
            subject_id = data[0]
            subject_title = data[1]
            break

    # add the grade for student in the subject
    grade_number = 0.0
    while True:
        grade_number = float(
            input(
                f"Enter the grade for '{student_name}' in '{subject_title}' subject : "
            )
        )

        if check_grade(grade_number):
            break
        else:
            print("Enter grade for student as a number ... !")

    # try add grade
    try:
        grade.Get_Query(
            f"INSERT INTO grades (grade, student_id, subject_id) VALUES({grade_number}, {student_id}, {subject_id})"
        )

        print(
            f"Adding grade for '{student_name}' in '{subject_title}' subject Successfuly Done ... !"
        )
    except:
        print("Adding grade Failed ... !")


# search the grades of a student in a specific subject
def search_grade() -> int:
    "search the grades of a student in a specific subject"

    # variables
    global grade
    ids = {"student": 0, "subject": 0}

    # get student and subject code for search the IDs
    while True:
        search = input("Enter the student or subject code (exp: code): ")

        # try to search IDs
        try:
            find_student = search_one_record(search, TABLE_STD)
            find_subject = search_one_record(search, TABLE_SBJ)

            # check witch one found
            if find_student:
                ids["student"] = find_student[0]

            if find_subject:
                ids["subject"] = find_subject[0]

            # show not found message if did not find anyone them
            if find_student == False and find_subject == False:
                print("Student or subject not found ... !")
            else:
                break

        except:
            print("Searching for student or subject Failed  ... !")

    # try to find the grades of the student or specific subject
    try:
        data = grade.Get_Query(
            f"""
            SELECT grades.id, grades.grade,
            students.firstname || ' ' || students.lastname as student_name,
            subjects.title
            FROM grades, students, subjects
            WHERE (grades.student_id={ids['student']} OR grades.subject_id={ids['subject']})
            AND grades.student_id=students.id AND grades.subject_id=subjects.id
            """,
            fetch_result=True,
        )

        if data != []:
            table(data, ["ID"] + COLUMNS, True)
            return 1
        else:
            print("Grades not found ... !")
            return 0

    except:
        print("Searching for grade Failed ... !")
        return 0


# edit the grade of a student or specific subject
def edit_grade() -> int:
    "edit the grade of a student or specific subject"

    # search for the grade
    search_grade()

    # get the grade ID for edit
    flag_valid_grade = False
    grade_id = 0

    while True:

        try:
            grade_id = int(input("Enter the grade ID that should edit : "))

            # get new grade for the grade
            while True:
                new_grade = float(
                    input(
                        f"Enter the new grade for grade with '{grade_id}' ID (-1 to enter ID again) : "
                    )
                )

                if new_grade == -1:  # check if user want to enter grade ID again
                    break
                elif check_grade(new_grade):  # check the new grade is valid
                    flag_valid_grade = True
                    break
                else:
                    print("This new grade is not valid ... !")

            # check grade if ok and not enter grade ID again
            if flag_valid_grade:
                break

        except:
            print("Enter grade_ID and new grade as number ... !")

    # try to edit the grade
    try:
        grade.Get_Query(f"UPDATE grades SET grade={new_grade} WHERE id={grade_id}")
        print("The grade Successfuly Done ... !")

        return 1

    except:
        print("Editing the grade Failed ... !")
        return 0


# delete the grade of a student or specific subject
def delete_grade() -> int:
    "delete the grade of a student or specific subject"

    # search for the grade
    search_grade()

    # choice a grade to delete
    grade_id = 0
    while True:
        try:
            grade_id = int(input("Enter the ID of grade for delete : "))

            if check_number_greater_zero(grade_id, True):
                break
            else:
                print("Entered ID is not valid ... !")
        except:
            print("Enter the ID as number ... !")

    # try to delete the grade
    try:
        grade.Get_Query(f"DELETE FROM grades WHERE id={grade_id}")

        print("The grade Successfuly deleted ... !")
        return 1

    except:
        print("Deleting the grade Failed ... !")
        return 0
