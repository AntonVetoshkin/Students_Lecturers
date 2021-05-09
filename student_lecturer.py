class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and grade in range(10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and grade in range(10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


pet_iv = Student('Petr', 'Ivanov', 'Male')
mark_z_l = Lecturer('Mark', 'Zoo')
mark_z_l.courses_attached = 'Pyton'
pet_iv.add_courses(['HTML', 'C++'])
pet_iv.courses_in_progress = ['Pyton', 'CSS']
pet_iv.rate_lec(mark_z_l, 'Pyton', 9)
kris_lee_r = Reviewer('Kriss', 'Lee')
kris_lee_r.courses_attached = ['Pyton', 'CSS', 'C++']
kris_lee_r.rate_hw(pet_iv, 'Pyton', 7)
kris_lee_r.rate_hw(pet_iv, 'Pyton', 5)
pet_iv.rate_lec(kris_lee_r, 'Pyton', 3)
kris_lee_r.rate_hw(pet_iv, 'C++', 2)
kris_lee_r.rate_hw(pet_iv, 'CSS', 8)
print(pet_iv.__dict__)
print(mark_z_l.__dict__)
print(kris_lee_r.__dict__)
