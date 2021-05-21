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

    def average_grade(self):
        average_list = {}
        for course, mark in self.grades.items():
            average = int((sum(mark) / len(mark)))
            average_list[course] = average
        return sorted(average_list.items())

    def __str__(self):
        print('Имя: ' + self.name)
        print('Фамилия: ' + self.surname)
        print(self.average_grade())
        print('Курсы в процессе изучения: ')
        print(self.courses_in_progress)
        print('Завершенные курсы: ')
        print(self.finished_courses)
        return

    def __lt__(self, other):
        if self.average_grade() > other.average_grade():
           print('больше')
        elif self.average_grade() < other.average_grade():
           print('меньше')
        else:
            print('равно')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def average_grade(self):
        average_list = {}
        for course, mark in self.grades.items():
            average = int((sum(mark) / len(mark)))
            average_list[course] = average
        return sorted(average_list.items())

    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + self.average_grade() + '\n')

    def __lt__(self, other):
        if self.average_grade() > other.average_grade():
           print('больше')
        elif self.average_grade() < other.average_grade():
           print('меньше')
        else:
            print('равно')



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

    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n')

pet_iv = Student('Petr', 'Ivanov', 'Male')
pet_iv.add_courses(['HTML', 'C++'])
pet_iv.courses_in_progress = ['Pyton', 'CSS']
vas_se = Student('Vasiliy', 'Semenov', 'Male')
vas_se.add_courses(['HTML'])
vas_se.courses_in_progress = ['Pyton']
mark_z_l = Lecturer('Mark', 'Zoo')
mark_z_l.courses_attached = 'Pyton'
den_braun_l = Lecturer('Den', 'Braun')
den_braun_l.courses_attached = ['Pyton', 'CSS']
kris_lee_r = Reviewer('Kriss', 'Lee')
kris_lee_r.courses_attached = ['Pyton', 'CSS', 'C++']
kris_lee_r.rate_hw(pet_iv, 'Pyton', 7)
kris_lee_r.rate_hw(pet_iv, 'Pyton', 5)
pet_iv.rate_lec(den_braun_l, 'CSS', 5)
pet_iv.rate_lec(den_braun_l, 'CSS', 3)
kris_lee_r.rate_hw(pet_iv, 'C++', 2)
kris_lee_r.rate_hw(pet_iv, 'CSS', 8)
si_shen_r = Reviewer('Si', 'Shen')
si_shen_r.courses_attached = ['Pyton', 'CSS']
si_shen_r.rate_hw(vas_se, 'Pyton', 4)
si_shen_r.rate_hw(vas_se, 'Pyton', 2)
pet_iv.rate_lec(mark_z_l, 'Pyton', 9)
pet_iv.rate_lec(mark_z_l, 'Pyton', 7)
vas_se.rate_lec(den_braun_l, 'Pyton', 9)
vas_se.rate_lec(den_braun_l, 'Pyton', 5)

print(pet_iv.average_grade())
print(vas_se.average_grade())
print(mark_z_l < den_braun_l)
print(pet_iv < vas_se)