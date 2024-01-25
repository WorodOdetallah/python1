from Lecturer import *


class CourseManager(Lecturer):
    def __init__(self, id: int, first_name: str, last_name: str, employee_number: int, seniority, salary: int,
                 course_lecturers: list):
        super(CourseManager, self).__init__(id, first_name, last_name, employee_number, seniority, salary)
        self.course_lecturers = course_lecturers

    @property
    def course_lecturers(self):
        return self.__course_lecturers

    @course_lecturers.setter
    def course_lecturers(self, course_lecturers: list):
        self.__course_lecturers = course_lecturers

    def teach_class(self, student_list: list):
        print("teaching class")

    def manage_course(self):
        print("course managed")

    def __str__(self):
        return super(CourseManager, self).__str__() + \
               "\n The course lecturers: " + self.__course_lecturers
