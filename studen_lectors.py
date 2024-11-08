class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка' 
    
    def __mid_grade(self):
        list_grades = sum(list(self.grades.values()), [])
        return round(sum(list_grades) / len(list_grades), 1)
        
    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__mid_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'''
    
    def __lt__(self, other):
        return self.__mid_grade() < other.__mid_grade()
    def __le__(self, other):
        return self.__mid_grade() <= other.__mid_grade()
    def __gt__(self, other):
        return self.__mid_grade() > other.__mid_grade()
    def __ge__(self, other):
        return self.__mid_grade() >= other.__mid_grade()
    def __eq__(self, other):
        return self.__mid_grade() == other.__mid_grade()
    def __ne__(self, other):
        return self.__mid_grade() != other.__mid_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

     
class Lecturer(Mentor):
    def __init__(self, name, surname):
       super().__init__(name, surname)
       self.courses_attached = []
       self.grades_from_students = {}

    def __mid_grade(self):
        list_grades = sum(list(self.grades_from_students.values()), [])
        return round(sum(list_grades) / len(list_grades), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__mid_grade()}'
    
    def __lt__(self, other):
        return self.__mid_grade() < other.__mid_grade()
    def __le__(self, other):
        return self.__mid_grade() <= other.__mid_grade()
    def __gt__(self, other):
        return self.__mid_grade() > other.__mid_grade()
    def __ge__(self, other):
        return self.__mid_grade() >= other.__mid_grade()
    def __eq__(self, other):
        return self.__mid_grade() == other.__mid_grade()
    def __ne__(self, other):
        return self.__mid_grade() != other.__mid_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
    
def students_mid_grade(course, students):
    grade_list = []
    for student in students:
        if course in student.grades:
            grade_list += student.grades[course]
    return round(sum(grade_list) / len(grade_list), 1)

def lecturers_mid_grade(course, lecturers):
    grade_list = []
    for lecturer in lecturers:
        if course in lecturer.grades_from_students:
            grade_list += lecturer.grades_from_students[course]
    return round(sum(grade_list) / len(grade_list), 1)
    

some_student1 = Student('Ruoy', 'Eman', 'male')
some_student2 = Student('Oleg', 'Petrov', 'male')
some_lecturer1 = Lecturer('Mikhail', 'Ivanov')
some_lecturer2 = Lecturer('Nicolai', 'Ivashov')
some_reviewer1 = Reviewer('Petr', 'Titiov')
some_reviewer2 = Reviewer('Some', 'Buddy')

some_student1.finished_courses = ['Введение в программирование']
some_student1.courses_in_progress = ['Git', 'Python']
some_student1.grades = {'Git': [10,10, 10, 10,10], 'Python': [10,10, 10, 10,10]}
print(some_student1)
print('-' * 10)

some_student2.finished_courses = []
some_student2.courses_in_progress = ['Java', 'Python']
some_student2.grades = {'Java': [10, 10, 10, 10,10], 'Python': [10,10,10, 10,10]}
print(some_student2)
print('-' * 10)

print(some_student1 > some_student2, some_student1 < some_student2, some_student1 == some_student2, sep='\n')
print('-' * 10)

some_lecturer1.courses_attached = ['Git', 'Python']
some_student1.rate_lect(some_lecturer1, 'Git', 9.9)
some_student2.rate_lect(some_lecturer1, 'Python', 9.9)
print(some_lecturer1)
print('-' * 10)

some_lecturer2.courses_attached = ['Java']
some_lecturer2.grades_from_students = {'Java': [9, 9]}
print(some_lecturer2)
print('-' * 10)

print(some_lecturer1 > some_lecturer2, some_lecturer1 < some_lecturer2, some_lecturer1 == some_lecturer2, sep='\n')
print('-' * 10)

some_reviewer1.courses_attached = ['Git', 'Java']
print(some_reviewer1)
print('-' * 10)

some_reviewer2.courses_attached = ['Python']
some_reviewer2.rate_hw(some_student1, 'Python', 9)
print(some_reviewer2, some_student1, sep='\n'*2)
print('-' * 10)

all_students = [some_student1, some_student2]
all_lecturers = [some_lecturer1, some_lecturer2]
print(f"Средняя оценка студентов по курсу 'Python' - {students_mid_grade('Python', all_students)}")
print(f"Средняя оценка лекторов по курсу 'Git' - {lecturers_mid_grade('Git', all_lecturers)}")


        

   
