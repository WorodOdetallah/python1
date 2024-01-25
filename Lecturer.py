from Employee import *


class Lecturer(Employee,Ilecturing):
    def __init__(self, id:int, first_name: str, last_name: str, employee_number: int, seniority, salary: int):
        super(Lecturer, self).__init__(id, first_name, last_name, employee_number)
        self.seniority = seniority
        self.salary = salary

    @property
    def seniority(self):
        return self.__seniority

    @seniority.setter
    def seniority(self, seniority):
        self.__seniority = seniority

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def teach_class(self, students_list: list):
        print("class Lecture")

    def __str__(self):
        return super(Lecturer, self).__str__() + \
               "\nThe Salary: " + str(self.__salary) + \
               "\nThe Seniority: " + str(self.__seniority)



