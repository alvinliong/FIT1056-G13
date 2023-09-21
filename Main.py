"""
Run this file to start CodeVenture
"""

from User import User
from Student import Student
from Teacher import Teacher
from StudentProgress import StudentProgress


def read_user_database():
    """
    Reads the data files and updates the global variables
    :return: None

    """
    global students_database
    global teachers_database

    students_database = []
    teachers_database = []
    path = "./data/users.txt"

    try:
        file = open(path, "r", encoding="utf8")
        lines = list(file)

        for line in lines:
            (user_type,
             first_name,
             last_name,
             email,
             phone_number,
             date_of_birth,
             username,
             password) = line.strip("\n").split(",")

            if (user_type == "student"):
                student = Student(first_name,
                                  last_name,
                                  email,
                                  phone_number,
                                  date_of_birth,
                                  username,
                                  password)
                students_database.append(student)
            elif (user_type == "teacher"):
                teacher = Teacher(first_name,
                                  last_name,
                                  email,
                                  phone_number,
                                  date_of_birth,
                                  username,
                                  password)
                teachers_database.append(teacher)
            else:
                "User type undefined."

        file.close()
    except FileNotFoundError:
        print("The users data file does not exist!")


def write_user_database(user_details):
    path = "./data/users.txt"
    data_string = ",".join(user_details)

    file = open(path, "a")
    file.write("\n" + data_string)
    file.close()


def clear_console():
    """
    Prints empty lines to clear the console
    :return: None
    """
    print("\n" * 5)


def main_menu():
    """
    This function prints all the menu options available to select in the main menu
    :return: None
    """
    clear_console()
    print("CodeVenture")
    print("=" * 50)
    print("\n")
    print("\t1. Register")
    print("\t2. Login")
    print("\t3. Exit")
    print("\n")


def register_menu():
    """
    This function prints the menu for register page
    :return: None
    """
    clear_console()
    print("Register")
    print("=" * 50)
    print("\n")
    print("Register a new account with CodeVenture. CTRL+C to return to main menu at anytime.")
    print("\n")


def register_main():
    """
    This function runs the main logic for the register page
    :return: None
    """
    clear_console()
    register_menu()
    while True:
        valid_details = True
        try:
            print("What account would you like to register as?")
            print("\n")
            print("\t1. Student")
            print("\t2. Teacher")
            print("\n")
            user_input = input("Enter your option: ")
            if user_input == "1":
                user_type = "student"
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                phone_number = input(
                    "Enter your phone number (optional, press enter to skip): ")
                date_of_birth = input(
                    "Enter your date of birth (DD/MM/YYYY): ")
                username = input("Enter your chosen username: ")
                password = input("Enter your chosen password: ")
                for student in students_database:
                    if (student.get_username() == username or student.get_email() == email):
                        valid_details == "Username or email already exists"
                if (valid_details):
                    user_details = [user_type, first_name, last_name,
                                    email, phone_number, date_of_birth, username, password]
                    write_user_database(user_details)
                    read_user_database()
                    print("User registered!")
                    break
                else:
                    print(valid_details)

            elif user_input == "2":
                user_type = "teacher"
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                phone_number = input(
                    "Enter your phone number (optional, press enter to skip): ")
                date_of_birth = input(
                    "Enter your date of birth (DD/MM/YYYY): ")
                username = input("Enter your chosen username: ")
                password = input("Enter your chosen password: ")
                for student in students_database:
                    if (student.get_username() == username or student.get_email() == email):
                        valid_details == "Username or email already exists"
                if (valid_details):
                    user_details = [user_type, first_name, last_name,
                                    email, phone_number, date_of_birth, username, password]
                    write_user_database(user_details)
                    read_user_database()
                    print("User registered!")
                    break
                else:
                    print(valid_details)
            else:
                "Please enter a valid option."
        except KeyboardInterrupt:
            clear_console()
            print("Registration cancelled.")
            break


def login_menu():
    """
    This function prints the menu for login page
    :return: None
    """
    clear_console()
    print("Login")
    print("=" * 50)
    print("\n")
    print("Login to your CodeVenture account. CTRL+C to return to main menu at anytime.")
    print("\n")


def login_main():
    """
    This function runs the main logic for the login page
    :return: None
    """
    global current_user

    clear_console()
    login_menu()
    while True:
        user_found = False
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for student in students_database:
                if (student.get_username() == username and student.get_password() == password):
                    student.set_logged_in()
                    user_found = True
                    current_user = student

            for teacher in teachers_database:
                if (teacher.get_username() == username and teacher.get_password() == password):
                    teacher.set_logged_in()
                    user_found = True
                    current_user = teacher

            if (user_found == True):
                clear_console()
                print("Logged in!")
                if (current_user.get_user_type() == "student"):
                    student_main()
                elif (current_user.get_user_type() == "teacher"):
                    # teacher_main()
                    pass
                break

            else:
                print("Username or password is incorrect!")

        except KeyboardInterrupt:
            clear_console()
            print("Login cancelled.")
            break


def student_main_menu():
    """
    This function prints the menu for student main menu page
    :return: None
    """
    clear_console()
    print("CodeVenture - Student")
    print("=" * 50)
    print("\n")
    print("Welcome " + current_user.get_first_name() +
          " " + current_user.get_last_name())
    print("\n")
    print("\t1. Start module")
    print("\t2. Unit selection page")
    print("\t3. Attempt quiz")
    print("\t4. Settings")
    print("\t5. Q&A Forum")
    print("\t6. Logout")
    print("\n")


def student_main():
    """
    This function runs the main logic for the student main menu
    :return: None
    """

    clear_console()
    while True:
        # Print the menu options
        student_main_menu()
        menu_input = input("Please enter a menu option: ")

        if menu_input == "1":
            pass
        elif menu_input == "2":
            pass
        elif menu_input == "3":
            pass
        elif menu_input == "4":
            pass
        elif menu_input == "5":
            pass
        elif menu_input == "6":
            current_user.set_logged_out()
            print("Logging out!")
            break
        else:
            # Invalid input option
            print("You have not selected a valid menu option!",
                  "Please try again.")


def main():
    """
    This function handles all program logic related to the main menu.
    :return: None
    """

    # populate user database
    read_user_database()

    while True:
        # Print the mode options
        main_menu()
        menu_input = input("Please enter a menu option: ")

        if menu_input == "1":
            register_main()
        elif menu_input == "2":
            login_main()
        elif menu_input == "3":
            print("Exiting CodeVenture")
            break
        else:
            # Invalid input option
            print("You have not selected a valid menu option!",
                  "Please try again.")


if __name__ == "__main__":
    main()      # Execute the main() function if this file is run