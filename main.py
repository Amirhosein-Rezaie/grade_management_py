from tools.func import *
from msvcrt import getwch

# varialbes
flag_first_time_run = check_database_first_time()


# funcs
# # show the list of works
def list_of_works() -> int:
    "show the list of works"

    print("""
        (1) students management
        (2) subjects management
        (3) grades managements
        (4) analysis grades
        """)
    print("Enter the number of work [1,4] : ", flush=True, end="")
    while True:
        try:
            number = int(getwch())

            if number >= 1 and number <= 4:
                print(number)
                return number
        except:
            pass


# show the list of subworks base on list of works
def list_of_subworks(number_work: int):
    "show the list of subworks base on list of works"

    subworks_number = {
        1: 5,
        2: 5,
        3: 4,
        4: 1,
    }  # the max number that user can choice as subword for each of works
    subworks = {
        1: {
            "features": [
                "(1) Add",
                "(2) Delete",
                "(3) Edit",
                "(4) Search",
                "(5) Show all",
            ],
            "suffix": "student",
        },
        2: {
            "features": [
                "(1) Add",
                "(2) Delete",
                "(3) Edit",
                "(4) Search",
                "(5) Show all",
            ],
            "suffix": "Subject",
        },
        3: {
            "features": ["(1) Add", "(2) Delete", "(3) Edit", "(4) Search"],
            "suffix": "Grade",
        },
        4: {"features": ["(1) Avrg "], "suffix": "Student"},
    }

    # show the list of subworks
    print("\n" + "\t\t" + "(0) Go back")
    for value in subworks[number_work]["features"]:
        print("\t\t" + value + " " + subworks[number_work]["suffix"] + "(s)")

    print(
        "\n" + f"Enter the number of subwork [0,{subworks_number[number_work]}]: ",
        flush=True,
        end="",
    )
    while True:
        try:
            number = int(getwch())

            if number >= 0 and number <= subworks_number[number_work]:
                print(number)

                return number
        except:
            pass


# run the func of work base on the number that user entered
def perform_func(code_work: int, code_subwork: int) -> None:
    "run the func of work base on the number that user entered"

    # import the modules that include the features
    from students import features as student_features
    from subjects import features as subject_features
    from grades import features as grade_features

    # list of feature's functions
    func = {
        1: {
            1: student_features.add_student,
            2: student_features.delete_student,
            3: student_features.edit_student,
            4: student_features.search_student,
            5: student_features.show_all_students,
        },
        2: {
            1: subject_features.add_subject,
            2: subject_features.delete_subject,
            3: subject_features.edit_subject,
            4: subject_features.search_subject,
            5: subject_features.show_all_subjects,
        },
        3: {
            1: grade_features.add_grade,
            2: grade_features.delete_grade,
            3: grade_features.edit_grade,
            4: grade_features.search_grade,
        },
        4: {},
    }

    splitter_line()

    func[code_work][code_subwork]()

    splitter_line()


# main of program
def main() -> None:
    "main of program"

    global flag_first_time_run

    while True:

        # check database exists for realise to the program ran first time
        if flag_first_time_run == True:

            # try to create databse file and tables
            run_command(r"cls")
            try:
                start_database()
                print("Database created Successfuly ... !" + "\n")

                flag_first_time_run = False

                press_enter_to_continue()
            except:
                print("Creating database file Failed ... !" + "\n")
                press_enter_to_continue()
                continue

        # start the program
        run_command(r"cls")
        print("Welcome to Management of Grades and students App")

        # get the number of work from user
        code_work = list_of_works()
        code_subwork = list_of_subworks(code_work)

        if code_subwork == 0:
            continue

        perform_func(code_work, code_subwork)

        press_enter_to_continue()


if __name__ == "__main__":
    main()
