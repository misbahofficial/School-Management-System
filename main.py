import json


def add_teacher():
    teacher_id = input("Enter teacher ID: ")
    teacher_data = {
        'name': input("Enter teacher name: "),
        'designation': input("Enter teacher designation: "),
        'address': input("Enter teacher address: "),
        'email': input("Enter teacher E-mail: "),
        'specialization': input("Enter fields of specialization separated by spaces: ").split()
    }

    data = {}  # Initialize data dictionary here

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'teacher' not in data:  # Check if 'student' key exists
        data['teacher'] = {}  # Initialize 'student' key if it doesn't exist

    data['teacher'][teacher_id] = teacher_data

    with open('school_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Teacher {teacher_id} added successfully.")


def teacher_info(teacher_id):
    data = {}
    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'teacher' in data and teacher_id in data['teacher']:
        print(f"""    
    ----- Showing info of {data['teacher'][teacher_id]['name']} -----

    Teacher ID:   {teacher_id}
    Name:         {data['teacher'][teacher_id]['name']}
    designation:  {data['teacher'][teacher_id]['designation']}
    Email:        {data['teacher'][teacher_id]['email']}
    Address:      {data['teacher'][teacher_id]['address']}
    Specialization:{', '.join(map(str, data['teacher'][teacher_id]['specialization']))}
    """)
    else:
        print("Teacher not found!")


def edit_teacher_info(teacher_id):
    data = {}
    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'teacher' in data:
        if teacher_id in data['teacher']:
            to_edit = int(input('''
                What teacher info to edit?

                1. Name
                2. Designation
                3. Address
                4. Email
                5. Specialization
                >>> '''))

            if to_edit == 1:
                new_name = input("Enter new name: ")
                data['teacher'][teacher_id]['name'] = new_name
            elif to_edit == 2:
                new_designation = input("Enter new Designation: ")
                data['teacher'][teacher_id]['designation'] = new_designation
            elif to_edit == 3:
                new_address = input("Enter new Address: ")
                data['teacher'][teacher_id]['address'] = new_address
            elif to_edit == 4:
                new_email = input("Enter new Email: ")
                data['teacher'][teacher_id]['email'] = new_email
            elif to_edit == 5:
                new_specialization = input("Enter new Specialization: ")
                data['teacher'][teacher_id]['specialization'] = new_specialization
            else:
                print("Invalid command!")

            with open('school_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Teacher info successfully edited.")
        else:
            print("Teacher ID not found!")
    else:
        print("Teacher ID invalid!")


def remove_teacher(teacher_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'teacher' in data and teacher_id in data['teacher']:
        del data['teacher'][teacher_id]

        with open('school_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Teacher {teacher_id} removed successfully.")
    else:
        print(f"Teacher {teacher_id} not found.")


def student_info(student_id):
    data = {}
    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'student' in data and student_id in data['student']:
        print(f"""
    ----- Showing info of {data['student'][student_id]['name']} -----
    
    Student ID:   {student_id}
    Name:         {data['student'][student_id]['name']}
    Age:          {data['student'][student_id]['age']}
    Email:        {data['student'][student_id]['email']}
    Courses:      {', '.join(map(str, data['student'][student_id]['courses']))}
    """)
    else:
        print("Student not found!")


def add_student():
    student_id = input("Enter student ID: ")
    student_data = {
        'name': input("Enter student name: "),
        'age': int(input("Enter student age: ")),
        'email': input("Enter student E-mail: "),
        'courses': input("Enter courses separated by spaces: ").split()
    }

    data = {}  # Initialize data here

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    # After the try-except block, 'data' is either loaded from the file or an empty dictionary

    if 'student' not in data:  # Check if 'student' key exists
        data['student'] = {}  # Initialize 'student' key if it doesn't exist

    data['student'][student_id] = student_data

    with open('school_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Student {student_id} added successfully.")


def edit_student_info(student_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'student' in data:
        to_edit = int(input('''
    What student info to edit?

    1. Name
    2. Age
    3. Email
    4. Courses
        '''))

        if to_edit == 1:
            new_name = input("Enter new name: ")
            data['student'][student_id]['name'] = new_name
        elif to_edit == 2:
            new_age = int(input("Enter new age: "))
            data['student'][student_id]['age'] = new_age
        elif to_edit == 3:
            new_email = input("Enter new email: ")
            data['student'][student_id]['email'] = new_email
        elif to_edit == 4:
            new_courses = input("Enter new courses: ")
            data['student'][student_id]['courses'] = new_courses
        else:
            print("Invalid command!")

        with open('school_data.json', 'w') as f:
            json.dump(data, f, indent=4)

        print("Teacher info successfully edited.")

    else:
        print("Student ID invalid!")

def remove_student(student_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'student' in data and student_id in data['student']:
        del data['student'][student_id]

        with open('school_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Student {student_id} removed successfully.")
    else:
        print(f"Student {student_id} not found.")


def add_staff():
    data = {}

    staff_id = input("Enter staff ID: ")
    staff_data = {
        'name': input("Enter staff name: "),
        'age': int(input("Enter staff age: ")),
        'address': input("Enter staff address: "),
        'working-hour': input("Enter staff working hour: "),
        'salary': float(input("Enter staff salary: "))
    }

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'staff' not in data:
        data['staff'] = {}

    data['staff'][staff_id] = staff_data

    with open('school_data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Staff {staff_id} added successfully.")


def staff_info(staff_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'staff' in data and staff_id in data['staff']:
        print(f"""
    ----- Showing info of {data['staff'][staff_id]['name']} -----
    
    Staff ID:     {staff_id}
    Name:         {data['staff'][staff_id]['name']}
    Age:          {data['staff'][staff_id]['age']}
    Address:      {data['staff'][staff_id]['address']}
    Working Hour: {data['staff'][staff_id]['working-hour']}
    Salary:       {data['staff'][staff_id]['salary']}
    """)

def edit_staff_info(staff_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'staff' in data:
        to_edit = int(input('''
    What staff info to edit?
    
    1. Name
    2. Age
    3. Address
    4. Working Hour
    5. Salary
    >>>
        '''))
        if to_edit == 1:
            new_name = input("Enter new name: ")
            data['staff'][staff_id]['name'] = new_name
        elif to_edit == 2:
            new_age = int(input("Enter new age: "))
            data['staff'][staff_id]['age'] = new_age
        elif to_edit == 3:
            new_address = input("Enter new address: ")
            data['staff'][staff_id]['address'] = new_address
        elif to_edit == 4:
            new_working_hour = input("Enter new working hour: ")
            data['staff'][staff_id]['working-hour'] = new_working_hour
        elif to_edit == 5:
            new_salary = float(input("Enter new salary: "))
            data['staff'][staff_id]['salary'] = new_salary
        else:
            print("Invalid command!")

        with open('school_data.json', 'w') as f:
            json.dump(data, f, indent=4)

        print("Staff info successfully edited.")

    else:
        print("Staff ID invalid!")


def remove_staff(staff_id):
    data = {}

    try:
        with open('school_data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    if 'staff' in data and staff_id in data['staff']:
        del data['staff'][staff_id]

        with open('school_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Staff {staff_id} removed successfully.")
    else:
        print(f"Staff ID {staff_id} not found.")


while True:
    print('''
    1. Add Teacher
    2. Teacher Info
    3. Edit Teacher Info
    4. Remove Teacher
    5. Add Student
    6. Student Info
    7. Edit Student Info
    8. Remove Student
    9. Add Staff
    10. Staff Info
    11. Edit Staff Info
    12. Remove Staff
    13. Save & Exit
''')
    user_choice = int(input("Enter choice: "))

    if user_choice == 1:
        add_teacher()
        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break

    elif user_choice == 2:
        teacher_id = input("Enter teacher ID: ")
        teacher_info(teacher_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 3:

        teacher_id = input("Enter teacher ID: ")
        edit_teacher_info(teacher_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 4:
        teacher_id = input("Enter teacher ID: ")
        remove_teacher(teacher_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break

        # add_student()
        #
        # will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()
        #
        # if will_continue == 'y':
        #     continue
        # else:
        #     break
    elif user_choice == 5:
        add_student()

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 6:
        student_id = input("Enter student ID: ")
        student_info(student_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 7:
        student_id = input("Enter student ID: ")
        edit_student_info(student_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 8:
        student_id = input("Enter student ID: ")
        remove_student(student_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 9:
        add_staff()
        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break

    elif user_choice == 10:
        staff_id = input("Enter staff ID: ")
        staff_info(staff_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break

    elif user_choice == 11:
        staff_id = input("Enter staff ID: ")
        edit_staff_info(staff_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break

    elif user_choice == 12:
        staff_id = input("Enter staff ID: ")
        remove_staff(staff_id)

        will_continue = input("Press 'y' to continue or 'n' to quit: ").lower()

        if will_continue == 'y':
            continue
        else:
            break
    elif user_choice == 13:
        break
