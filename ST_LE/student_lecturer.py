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
        list_courses = average_list.items()
        return 'Средняя оценка за домашние задания: ' + str(list_courses)


    def __str__(self):
        print('Имя: ' + self.name)
        print('Фамилия: ' + self.surname)
        print(self.average_grade())
        print('Курсы в процессе изучения: ')
        print(self.courses_in_progress)
        print('Завершенные курсы: ')
        print(self.finished_courses)
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def average_grade(self):
        for mark in self.grades.values():
            average = int((sum(mark) / len(mark)))
        return 'Средняя оценка за лекции: ' + str(average) + ' баллов'

    def __str__(self):
        return ('Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + self.average_grade() + '\n')


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
pet_iv.rate_lec(mark_z_l, 'Pyton', 9)
pet_iv.rate_lec(mark_z_l, 'Pyton', 5)
vas_se = Student('Vasiliy', 'Semenov', 'Male')
vas_se.add_courses(['HTML'])
vas_se.courses_in_progress = ['Pyton']
vas_se.rate_lec(mark_z_l, 'Pyton', 9)
vas_se.rate_lec(mark_z_l, 'Pyton', 5)
mark_z_l = Lecturer('Mark', 'Zoo')
mark_z_l.courses_attached = 'Pyton'
den_braun_l = Lecturer('Den', 'Braun')
den_braun_l.courses_attached = 'CSS'
kris_lee_r = Reviewer('Kriss', 'Lee')
kris_lee_r.courses_attached = ['Pyton', 'CSS', 'C++']
kris_lee_r.rate_hw(pet_iv, 'Pyton', 7)
kris_lee_r.rate_hw(pet_iv, 'Pyton', 5)
pet_iv.rate_lec(kris_lee_r, 'Pyton', 3)
kris_lee_r.rate_hw(pet_iv, 'C++', 2)
kris_lee_r.rate_hw(pet_iv, 'CSS', 8)
si_shen_r = Reviewer('Si', 'Shen')
si_shen_r.courses_attached = ['Pyton', 'CSS']
print(pet_iv.__dict__)
print(mark_z_l.__dict__)
print(kris_lee_r.__dict__)
print(kris_lee_r)
print(mark_z_l)
print(pet_iv)
