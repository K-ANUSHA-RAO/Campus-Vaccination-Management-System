# Campus Vaccination Management System
""" 
Fields :- ['USN', 'Name', 'Age', 'Phone', 'Vaccine_Dose']
Fields :- ['FID', 'Name', 'Age', 'Phone', 'Vaccine_Dose']
1. Add Vaccinated Student/Faculty Details
2. View Vaccinated Students/Faculty Details
3. Update Vaccinated Student/Faculty Details
4. Generate Non vaccinated Students/Faculty File
5. Back To Previous Window
6. Quit
""" 

import csv
# Define global variables
student_fields = ['USN', 'Name', 'Age', 'Phone', 'Vaccine_Dose']
faculty_fields = ['FID', 'Name', 'Age', 'Phone', 'Vaccine_Dose']

# Student Database
cse_first_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_first_year_students.csv'
cse_second_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_second_year_students.csv'
cse_third_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_third_year_students.csv'
cse_fourth_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_fourth_year_students.csv'

ise_first_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_first_year_students.csv'
ise_second_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_second_year_students.csv'
ise_third_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_third_year_students.csv'
ise_fourth_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_fourth_year_students.csv'

ec_first_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_first_year_students.csv'
ec_second_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_second_year_students.csv'
ec_third_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_third_year_students.csv'
ec_fourth_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_fourth_year_students.csv'

civil_first_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_first_year_students.csv'
civil_second_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_second_year_students.csv'
civil_third_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_third_year_students.csv'
civil_fourth_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_fourth_year_students.csv'

mech_first_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_first_year_students.csv'
mech_second_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_second_year_students.csv'
mech_third_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_third_year_students.csv'
mech_fourth_year_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_fourth_year_students.csv'

# Faculty database
cse_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\FACULTY\cse_faculty.csv'
ise_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\FACULTY\ise_faculty.csv'
ec_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\FACULTY\ec_faculty.csv'
civil_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\FACULTY\civil_faculty.csv'
mech_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\FACULTY\mech_faculty.csv'

# Vaccinated Student Database
cse_first_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_first_year_vaccinated_students.csv'
cse_second_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_second_year_vaccinated_students.csv'
cse_third_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_third_year_vaccinated_students.csv'
cse_fourth_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_fourth_year_vaccinated_students.csv'

ise_first_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_first_year_vaccinated_students.csv'
ise_second_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_second_year_vaccinated_students.csv'
ise_third_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_third_year_vaccinated_students.csv'
ise_fourth_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_fourth_year_vaccinated_students.csv'

ec_first_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_first_year_vaccinated_students.csv'
ec_second_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_second_year_vaccinated_students.csv'
ec_third_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_third_year_vaccinated_students.csv'
ec_fourth_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_fourth_year_vaccinated_students.csv'

civil_first_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_first_year_vaccinated_students.csv'
civil_second_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_second_year_vaccinated_students.csv'
civil_third_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_third_year_vaccinated_students.csv'
civil_fourth_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_fourth_year_vaccinated_students.csv'

mech_first_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_first_year_vaccinated_students.csv'
mech_second_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_second_year_vaccinated_students.csv'
mech_third_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_third_year_vaccinated_students.csv'
mech_fourth_year_vaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_fourth_year_vaccinated_students.csv'

# Vaccinated Faculty database
cse_vaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\FACULTY\cse_vaccinated_faculty.csv'
ise_vaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\FACULTY\ise_vaccinated_faculty.csv'
ec_vaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\FACULTY\ec_vaccinated_faculty.csv'
civil_vaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\FACULTY\civil_vaccinated_faculty.csv'
mech_vaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\FACULTY\mech_vaccinated_faculty.csv'

# Unvaccinated Student Database
cse_first_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_first_year_unvaccinated_students.csv'
cse_second_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_second_year_unvaccinated_students.csv'
cse_third_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_third_year_unvaccinated_students.csv'
cse_fourth_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\STUDENTS\cse_fourth_year_unvaccinated_students.csv'

ise_first_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_first_year_unvaccinated_students.csv'
ise_second_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_second_year_unvaccinated_students.csv'
ise_third_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_third_year_unvaccinated_students.csv'
ise_fourth_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\STUDENTS\ise_fourth_year_unvaccinated_students.csv'

ec_first_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_first_year_unvaccinated_students.csv'
ec_second_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_second_year_unvaccinated_students.csv'
ec_third_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_third_year_unvaccinated_students.csv'
ec_fourth_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\STUDENTS\ec_fourth_year_unvaccinated_students.csv'

civil_first_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_first_year_unvaccinated_students.csv'
civil_second_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_second_year_unvaccinated_students.csv'
civil_third_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_third_year_unvaccinated_students.csv'
civil_fourth_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\STUDENTS\civil_fourth_year_unvaccinated_students.csv'

mech_first_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_first_year_unvaccinated_students.csv'
mech_second_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_second_year_unvaccinated_students.csv'
mech_third_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_third_year_unvaccinated_students.csv'
mech_fourth_year_unvaccinated_student_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\STUDENTS\mech_fourth_year_unvaccinated_students.csv'

# Unvaccinated Faculty database
cse_unvaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CSE\FACULTY\cse_unvaccinated_faculty.csv'
ise_unvaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\ISE\FACULTY\ise_unvaccinated_faculty.csv'
ec_unvaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\EC\FACULTY\ec_unvaccinated_faculty.csv'
civil_unvaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\CIVIL\FACULTY\civil_unvaccinated_faculty.csv'
mech_unvaccinated_faculty_database = 'C:\Users\K ANUSHA RAO\OneDrive\Desktop\code\Campus-Vaccination-Management-System\MECH\FACULTY\mech_unvaccinated_faculty.csv'

# Display Functions
def display_menu():
    print("-----------------------------------------")
    print(" Campus Vaccination Management System ")
    print("-----------------------------------------")
    print("1. Student")
    print("2. Faculty")

# Student Display Functions
def display1_students_menu():
    print("-------------------")
    print(" Select Branch ")
    print("-------------------")
    print("1. Computer Science Engineering")
    print("2. Information Science Engineering")
    print("3. Electronics And Communication Engineering")
    print("4. Civil Engineering")
    print("5. Mechanical Engineering")
    print("6. Back To Previous Window")
    print("7. Quit")

def display2_students_menu():
    print("-------------------------")
    print(" Select Year Of Study ")
    print("-------------------------")
    print("1. First Year")
    print("2. Second Year")
    print("3. Third Year")
    print("4. Fourth Year")
    print("5. Back To Previous Window")
    print("6. Quit")

def display3_students_menu():
    print("-------------------------------------------")
    print(" Welcome To Vaccination Management System ")
    print("-------------------------------------------")
    print("1. Add Vaccinated Student Details")
    print("2. View Vaccinated Students Details")
    print("3. Update Vaccinated Student Details")
    print("4. Generate Non Vaccinated Students File")
    print("5. Back To Previous Window")
    print("6. Quit")

# Faculty Display Functions
def display1_faculty_menu():
    print("-----------------")
    print(" Select Branch")
    print("-----------------")
    print("1. Computer Science Engineering")
    print("2. Information Science Engineering")
    print("3. Electronics And Communication Engineering")
    print("4. Civil Engineering")
    print("5. Mechanical Engineering")
    print("6. Back To Previous Window")
    print("7. Quit")

def display2_faculty_menu():
    print("-------------------------------------------")
    print(" Welcome To Vaccination Management System")
    print("-------------------------------------------")
    print("1. Add Vaccinated Faculty Details")
    print("2. View Vaccinated Faculty Details")
    print("3. Update Vaccinated Faculty Details")
    print("4. Generate Non Vaccinated Faculty File")
    print("5. Back To Previous Window")
    print("6. Quit")

# CSE Student Add Functions
def add_cse_1year_student():
    print("--------------------------")
    print("Add Student Information")
    print("--------------------------")
    global student_fields
    global cse_first_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_first_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_cse_2year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global cse_second_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_second_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_cse_3year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global cse_third_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_third_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_cse_4year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global cse_fourth_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(cse_fourth_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

# ISE Student Add Functions
def add_ise_1year_student():
    print("--------------------------")
    print("Add Student Information")
    print("--------------------------")
    global student_fields
    global ise_first_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_first_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ise_2year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ise_second_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_second_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ise_3year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ise_third_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_third_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ise_4year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ise_fourth_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ise_fourth_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

# EC Student Add Functions
def add_ec_1year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ec_first_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_first_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ec_2year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ec_second_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_second_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ec_3year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global ec_third_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_third_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_ec_4year_student():
    print("----------------------------")
    print("Add Student Information")
    print("----------------------------")
    global student_fields
    global ec_fourth_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(ec_fourth_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

# CIVIL Student Add Functions
def add_civil_1year_student():
    print("----------------------------")
    print("Add Student Information")
    print("----------------------------")
    global student_fields
    global civil_first_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(civil_first_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_civil_2year_student():
    print("----------------------------")
    print("Add Student Information")
    print("----------------------------")
    global student_fields
    global civil_second_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(civil_second_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_civil_3year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global civil_third_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(civil_third_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_civil_4year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global civil_fourth_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(civil_fourth_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

# MECH Student Add Functions
def add_mech_1year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global mech_first_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(mech_first_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_mech_2year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global mech_second_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(mech_second_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_mech_3year_student():
    print("----------------------------")
    print("Add Student Information")
    print("----------------------------")
    global student_fields
    global ec_third_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(mech_third_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

def add_mech_4year_student():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global student_fields
    global mech_fourth_year_vaccinated_student_database
    student_data=[]
    for field in student_fields:
        value=input("Enter"+field+":")
        student_data.append(value)
    with open(mech_fourth_year_vaccinated_student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data Added Successfuly!")
    input("Press Any Key To Continue")
    return

# CSE Faculty Add Function
def add_cse_faculty():
    print("---------------------------")
    print("Add Faculty Information")
    print("---------------------------")
    global faculty_fields
    global cse_vaccinated_faculty_database
    faculty_data=[]
    for field in faculty_fields:
        value=input("Enter"+field+":")
        faculty_data.append(value)
    with open(cse_vaccinated_faculty_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([faculty_data])
    print("Data Added Successfully!")
    input("Press Any Key To Continue")
    return

# ISE Faculty Add Function
def add_ise_faculty():
    print("----------------------------")
    print("Add Faculty Information")
    print("----------------------------")
    global faculty_fields
    global ise_vaccinated_faculty_database
    faculty_data=[]
    for field in faculty_fields:
        value=input("Enter"+field+":")
        faculty_data.append(value)
    with open(ise_vaccinated_faculty_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([faculty_data])
    print("Data Added Successfully!")
    input("Press Any Key To Continue")
    return

# EC Faculty Add Function
def add_ec_faculty():
    print("---------------------------")
    print("Add Faculty Information")
    print("---------------------------")
    global faculty_fields
    global ec_vaccinated_faculty_database
    faculty_data=[]
    for field in faculty_fields:
        value=input("Enter"+field+":")
        faculty_data.append(value)
    with open(ec_vaccinated_faculty_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([faculty_data])
    print("Data Added Successfully!")
    input("Press Any Key To Continue")
    return

# CIVIL Faculty Add Function
def add_civil_faculty():
    print("---------------------------")
    print("Add Faculty Information")
    print("---------------------------")
    global faculty_fields
    global civil_vaccinated_faculty_database
    faculty_data=[]
    for field in faculty_fields:
        value=input("Enter"+field+":")
        faculty_data.append(value)
    with open(civil_vaccinated_faculty_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([faculty_data])
    print("Data Added Successfully!")
    input("Press Any Key To Continue")
    return

# MECH Faculty Add Function
def add_mech_faculty():
    print("--------------------------")
    print("Add Faculty Information")
    print("--------------------------")
    global faculty_fields
    global mech_vaccinated_faculty_database
    faculty_data=[]
    for field in faculty_fields:
        value=input("Enter"+field+":")
        faculty_data.append(value)
    with open(mech_vaccinated_faculty_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([faculty_data])
    print("Data Added Successfully!")
    input("Press Any Key To Continue")
    return

# CSE Students View Function
def view_cse_1year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global cse_first_year_vaccinated_student_database
    with open(cse_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_cse_2year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global cse_second_year_vaccinated_student_database
    with open(cse_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_cse_3year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global cse_third_year_vaccinated_student_database
    with open(cse_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_cse_4year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global cse_fourth_year_vaccinated_student_database
    with open(cse_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# ISE Students View Function
def view_ise_1year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ise_first_year_vaccinated_student_database
    with open(ise_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ise_2year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ise_second_year_vaccinated_student_database
    with open(ise_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ise_3year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ise_third_year_vaccinated_student_database
    with open(ise_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ise_4year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ise_fourth_year_vaccinated_student_database
    with open(ise_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# EC Students View Function
def view_ec_1year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ec_first_year_vaccinated_student_database
    with open(ec_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ec_2year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ec_second_year_vaccinated_student_database
    with open(ec_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ec_3year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ec_third_year_vaccinated_student_database
    with open(ec_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_ec_4year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global ec_fourth_year_vaccinated_student_database
    with open(ec_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# CIVIL Students View Function
def view_civil_1year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global civil_first_year_vaccinated_student_database
    with open(civil_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_civil_2year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global civil_second_year_vaccinated_student_database
    with open(civil_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_civil_3year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global civil_third_year_vaccinated_student_database
    with open(civil_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_civil_4year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global civil_fourth_year_vaccinated_student_database
    with open(civil_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# MECH Students View Function
def view_mech_1year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global mech_first_year_vaccinated_student_database
    with open(mech_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_mech_2year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global mech_second_year_vaccinated_student_database
    with open(mech_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_mech_3year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global mech_third_year_vaccinated_student_database
    with open(mech_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

def view_mech_4year_student():
    print("------------------")
    print("Student Records")
    print("------------------")
    global student_fields
    global mech_fourth_year_vaccinated_student_database
    with open(mech_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# CSE Faculty View functions
def view_cse_faculty():
    print("------------------")
    print("Faculty Records")
    print("------------------")
    global faculty_fields
    global cse_vaccinated_faculty_database
    with open(cse_vaccinated_faculty_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# ISE Faculty View functions
def view_ise_faculty():
    print("------------------")
    print("Faculty Records")
    print("------------------")
    global faculty_fields
    global ise_vaccinated_faculty_database
    with open(ise_vaccinated_faculty_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")

# EC Faculty View functions
def view_ec_faculty():
    print("------------------")
    print("Faculty Records")
    print("------------------")
    global faculty_fields
    global ec_vaccinated_faculty_database
    with open(ec_vaccinated_faculty_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")       

# CIVIL Faculty View functions
def view_civil_faculty():
    print("------------------")
    print("Faculty Records")
    print("------------------")
    global faculty_fields
    global civil_vaccinated_faculty_database
    with open(civil_vaccinated_faculty_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue") 

# MECH Faculty View functions
def view_mech_faculty():
    print("------------------")
    print("Faculty Records")
    print("------------------")
    global faculty_fields
    global mech_vaccinated_faculty_database
    with open(mech_vaccinated_faculty_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press Any Key To Continue")    

# CSE Student Update Functions
def update_cse_1year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global cse_first_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(cse_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(cse_first_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_cse_2year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global cse_second_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(cse_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(cse_second_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_cse_3year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global cse_third_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(cse_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(cse_third_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_cse_4year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global cse_fourth_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(cse_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(cse_fourth_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

# ISE Student Update Functions
def update_ise_1year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ise_first_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ise_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ise_first_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ise_2year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ise_second_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ise_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ise_second_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ise_3year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ise_third_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ise_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ise_third_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ise_4year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ise_fourth_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ise_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ise_fourth_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

# EC Student Update Functions
def update_ec_1year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ec_first_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ec_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ec_first_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ec_2year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ec_second_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ec_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ec_second_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ec_3year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ec_third_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ec_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ec_third_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_ec_4year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global ec_fourth_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(ec_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(ec_fourth_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

# CIVIL Student Update Functions
def update_civil_1year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global civil_first_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(civil_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(civil_first_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_civil_2year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global civil_second_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(civil_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(civil_second_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_civil_3year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global civil_third_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(civil_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(civil_third_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_civil_4year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global civil_fourth_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(civil_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(civil_fourth_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

# MECH Student Update Functions
def update_mech_1year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global mech_first_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(mech_first_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(mech_first_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_mech_2year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global mech_second_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(mech_second_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(mech_second_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_mech_3year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global mech_third_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(mech_third_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(mech_third_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

def update_mech_4year_student():
    print("------------------")
    print("Update Student")
    print("------------------")
    global student_fields
    global mech_fourth_year_vaccinated_student_database
    USN=input("Enter USN To Update: ")
    index_student=None
    updated_data=[]
    with open(mech_fourth_year_vaccinated_student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0 :
                if USN==row[0] :
                    index_student=counter
                    print("Student Found: At Index ",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter "+field+": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter=counter+1
    
    # To Check If Record Is Found Or Not
    if index_student is not None:
        with open(mech_fourth_year_vaccinated_student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("USN Not Found In The Database.")
    input("Press Any Key To Continue.")

# Generate Function For CSE Students