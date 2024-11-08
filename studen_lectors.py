class Student:
    def _init_ (self, l_name, f_name, group, gender):
        self.l_name = l_name
        self.f_name = f_name
        self.gender = gender
        self.group = group
        self.finished_courses = []  
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def _init_ (self, l_name, f_name):
        self.l_name = l_name
        self.f_name = f_name
        self.courses_attached = []
    
class Lectorer(Mentor):
    def _init_ (self, l_name, f_name):
        super(). __init__(l_name, f_name, )
        self.courses_attached = []

class Reviewer(Mentor):
    def _init_(self, l_name, f_name):
         super()._init_(l_name, f_name)
         self.courses_attached = []

    
        


