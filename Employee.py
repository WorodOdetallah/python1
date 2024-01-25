from abc import *
from Person import *


class Employee(ABC, Person):
    def __init__(self, id: int, first_name: str, last_name: str, employee_number: int):
        super(Employee, self).__init__(id, first_name, last_name)
        self.__employee_number = employee_number

    @property
    def employee_number(self):
        return self.__employee_number

    @employee_number.setter
    def employee_number(self, em_number):
        self.__employee_number = em_number

    def __str__(self):
        return super(Employee, self).__str__() + \
               "\nThe Employee Number: " + str(self.__employee_number)

