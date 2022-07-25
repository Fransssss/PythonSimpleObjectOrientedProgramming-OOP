# author: Fransiskus Agapa
from student import Student  # this calls the student class

print("\n== OOP Simple Menu ==")
print("1. Input data of a student")
print("2. Display student's name")
print("3. Display student's age")
print("4. Display student's year")
print("5. Display student's full data")
print("E. Exit")
choice = input("choice: ")

student = Student("Noname", 0, "NoYear")
confirm_change = False

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Input data of a student ]\n")
        name = ""
        name = input("input name: ")
        if name[0].islower():
            name = name.capitalize()          # capitalize user input
        age = 0
        print("input age: ", end=" ")
        age = input()
        year = ""
        year = input("year in school: ")
        student = Student(name, age, year)    # update data of a student
        confirm_change = True
        print("\n[ Data updated ]")

    elif choice == '2':
        print("\n[ Display student's name ]\n")
        print(student.the_name())

    elif choice == '3':
        print("\n[ Display student's age ]\n")
        print(student.the_age())

    elif choice == '4':
        print("\n[ Display student's year ]\n")
        print(student.the_year())

    elif choice == '5':
        print("\n[ Display student's full data ]\n")
        if confirm_change:
            print(student.the_information())
        else:
            print("[ No Data ]\n" ,student.name, student.age, student.year)

    else:
        print("\n[ Invalid choice ]")

    print("\n== OOP Simple Menu ==")
    print("1. Input data of a student")
    print("2. Display student's name")
    print("3. Display student's age")
    print("4. Display student's year")
    print("5. Display student's full data")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")

