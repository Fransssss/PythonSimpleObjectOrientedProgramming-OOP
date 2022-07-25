class Student:

    def __init__(self, name, age, year):  # self means the object that uses it
        self.name = name
        self.age = age
        self.year = year

    def the_name(self):
        print("The student's name is " + self.name)

    def the_age(self):
        print(self.name + " is " + str(self.age) + " year old")

    def the_year(self):
        print(self.name + " is in " + self.year + " year")

    def the_information(self):
        print("The student name is " + self.name + "!\n" + self.name + " is " + str(
            self.age) + " years old.\n" + self.name + " is in " + self.year + " year!\n" + self.name + " is an "
                                                                                                      "excellent "
                                                                                                      "student!")
