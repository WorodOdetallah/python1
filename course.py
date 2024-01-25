import Lecturer
import Student


class course:
    def __init__(self, course_id, course_name, course_manager, lecturer_list, students_list):
        self.course_id = course_id
        self.course_name = course_name
        self.course_manager = course_manager
        self.lecturer_list = lecturer_list
        self.students_list = students_list


  def course_id(self):
 return self.__course_id


