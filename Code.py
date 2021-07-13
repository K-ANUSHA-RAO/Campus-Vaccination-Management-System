# Campus Vaccination Management System
""" 
Fields :- ['USN', 'Name', 'Age', 'Phone', 'Vaccine_Dose']
1. Add Vaccinated Student/Faculty Details
2. View Vaccinated Students/Faculty Details
3. Update Vaccinated Student/Faculty Details
4. Generate Non vaccinated Students/Faculty File
5. Back To Previous Window
6. Quit
""" 

import csv
# Define global variables
student_fields = ['USN', 'Name', 'Age',  'Phone', 'Vaccine_Dose']
faculty_fields = ['FID', 'Name', 'Age',  'Phone', 'Vaccine_Dose']

cse_first_year_student_database = 'cse_first_year_students.csv'
cse_second_year_student_database = 'cse_second_year_students.csv'
cse_third_year_student_database = 'cse_third_year_students.csv'
cse_fourth_year_student_database = 'cse_fourth_year_students.csv'

ise_first_year_student_database = 'ise_first_year_students.csv'
ise_second_year_student_database = 'ise_second_year_students.csv'
ise_third_year_student_database = 'ise_third_year_students.csv'
ise_fourth_year_student_database = 'ise_fourth_year_students.csv'

ec_first_year_student_database = 'ec_first_year_students.csv'
ec_second_year_student_database = 'ec_second_year_students.csv'
ec_third_year_student_database = 'ec_third_year_students.csv'
ec_fourth_year_student_database = 'ec_fourth_year_students.csv'

civil_first_year_student_database = 'civil_first_year_students.csv'
civil_second_year_student_database = 'civil_second_year_students.csv'
civil_third_year_student_database = 'civil_third_year_students.csv'
civil_fourth_year_student_database = 'civil_fourth_year_students.csv'

mech_first_year_student_database = 'mech_first_year_students.csv'
mech_second_year_student_database = 'mech_second_year_students.csv'
mech_third_year_student_database = 'mech_third_year_students.csv'
mech_fourth_year_student_database = 'mech_fourth_year_students.csv'

cse_faculty_database = 'cse_faculty.csv'
ise_faculty_database = 'ise_faculty.csv'
ec_faculty_database = 'ec_faculty.csv'
civil_faculty_database = 'civil_faculty.csv'
mech_faculty_database = 'mech_faculty.csv'

# Display Functions
def display_menu():
    print("-----------------------------------------")
    print(" Campus Vaccination Management System")
    print("-----------------------------------------")
    print("1. Student")
    print("2. Faculty")

# Student Display Functions
def display1_students_menu():
    print("--------------------------------------")
    print(" Select Branch")
    print("---------------------------------------")
    print("1. Computer Science Engineering")
    print("2. Information Science Engineering")
    print("3. Electronics And Communication Engineering")
    print("4. Civil Engineering")
    print("5. Mechanical Engineering")
    print("6. Back To Previous Window")
    print("7. Quit")

def display2_students_menu():
    print("--------------------------------------")
    print("Select Year Of Study ")
    print("--------------------------------------")
    print("1. First Year")
    print("2. Second Year")
    print("3. Third Year")
    print("4. Fourth Year")
    print("5. Back To Previous Window")
    print("6. Quit")

def display3_students_menu():
    print("--------------------------------------")
    print(" Welcome To Vaccination Management System")
    print("---------------------------------------")
    print("1. Add Vaccinated Student Details")
    print("2. View Vaccinated Students Details")
    print("3. Update Vaccinated Student Details")
    print("4. Generate Non Vaccinated Students File")
    print("5. Back To Previous Window")
    print("6. Quit")

# Faculty Display Functions
def display1_faculty_menu():
    print("--------------------------------------")
    print(" Select Branch")
    print("---------------------------------------")
    print("1. Computer Science Engineering")
    print("2. Information Science Engineering")
    print("3. Electronics And Communication Engineering")
    print("4. Civil Engineering")
    print("5. Mechanical Engineering")
    print("6. Back To Previous Window")
    print("7. Quit")

def display2_faculty_menu():
    print("--------------------------------------")
    print(" Welcome To Vaccination Management System")
    print("---------------------------------------")
    print("1. Add Vaccinated Faculty Details")
    print("2. View Vaccinated Faculty Details")
    print("3. Update Vaccinated Faculty Details")
    print("4. Generate Non Vaccinated Faculty File")
    print("5. Back To Previous Window")
    print("6. Quit")

# CSE Student Add Functions
def add_cse_1year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global cse_first_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_first_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_cse_2year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global cse_second_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_second_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_cse_3year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global cse_third_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_third_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_cse_4year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global cse_fourth_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_fourth_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

# ISE Student Add Functions
def add_ise_1year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ise_first_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_first_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ise_2year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ise_second_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_second_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ise_3year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ise_third_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_third_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ise_4year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ise_fourth_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_fourth_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

# EC Student Add Functions
def add_ec_1year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ec_first_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_first_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ec_2year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ec_second_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_second_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ec_3year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ec_third_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_third_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

def add_ec_4year_student():
    print("---------------------------------------")
    print("Add Student Information")
    print("---------------------------------------")
    global student_fields
    global ec_fourth_year_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_fourth_year_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key to Continue")
    return

    