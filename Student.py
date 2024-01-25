from Person import *


class Student(Person):
    def __init__(self, id: int, first_name: str, last_name: str, student_number: int):
        super(Student, self).__init__(id, first_name, last_name)
        self.student_number = student_number

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, student_num):
        self.__student_number = student_num

    def home_work_report(self):
        print("Home Work has been submitted")

    def __str__(self):
        return super(Student, self).__str__() + "\nThe Student Number: " + str(self.__student_number)
