class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}
        self.finished_courses = []

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades_avg()}\nКурсы '
            f'в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return print(self.grades_avg() < other.grades_avg())

    def grades_avg(self):
        number_of_grades = 0
        sum_of_grades = 0
        for val in self.grades.values():
            number_of_grades += len(val)
            sum_of_grades += sum(val)
        return sum_of_grades / number_of_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades_avg()}'

    def __lt__(self, other):
        return print(self.grades_avg() < other.grades_avg())

    def grades_avg(self):
        number_of_grades = 0
        sum_of_grades = 0
        for val in self.grades.values():
            number_of_grades += len(val)
            sum_of_grades += sum(val)
        return sum_of_grades / number_of_grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

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


def avg_grades_hw_course(students, course):
    grades = 0
    num_grades = 0
    for student in students:
        for student_course in student.grades.keys():
            if student_course == course:
                for grade in student.grades.get(student_course):
                    grades += grade
                    num_grades += 1
    return grades / num_grades


def avg_grades_lect_course(lecturers, course):
    grades = 0
    num_grades = 0
    for lecturer in lecturers:
        for lecturer_course in lecturer.grades.keys():
            if lecturer_course == course:
                for grade in lecturer.grades.get(lecturer_course):
                    grades += grade
                    num_grades += 1
    return grades / num_grades


stud1 = Student("Мирослав", "Лопаткин")
stud2 = Student("Кира", "Полянина")
stud3 = Student("Антон", "Северный")

stud1.courses_in_progress += ['Математика']
stud1.courses_in_progress += ['Литература']
stud2.courses_in_progress += ['Литература']
stud3.courses_in_progress += ['Математика']
stud3.courses_in_progress += ['Письмо']

stud1.finished_courses += ['Акробатика']
stud2.finished_courses += ['Скалолазание']
stud3.finished_courses += ['Акробатика']

rev = Reviewer('Аксинья', 'Александрова')
rev2 = Reviewer('Севастьян', 'Пушкин')
rev.courses_attached += ['Математика']
rev.courses_attached += ['Литература']
rev2.courses_attached += ['Письмо']
lect1 = Lecturer("Даниил", "Сержак")
lect1.courses_attached += ['Математика']
lect1.courses_attached += ['Литература']
lect2 = Lecturer("Потап", "Ольхов")
lect2.courses_attached += ['Письмо']
lect2.courses_attached += ['Математика']

rev.rate_hw(stud1, 'Математика', 7)
rev.rate_hw(stud1, 'Литература', 3)
rev.rate_hw(stud1, 'Математика', 2)
rev.rate_hw(stud1, 'Математика', 4)

rev.rate_hw(stud2, 'Литература', 7)

rev.rate_hw(stud3, 'Математика', 3)
rev2.rate_hw(stud3, 'Письмо', 8)
rev.rate_hw(stud3, 'Математика', 7)
rev.rate_hw(stud3, 'Математика', 5)

stud1.rate_l(lect1, 'Математика', 7)
stud1.rate_l(lect2, 'Математика', 4)
stud2.rate_l(lect1, 'Литература', 5)
stud1.rate_l(lect1, 'Литература', 6)

stud3.rate_l(lect2, 'Письмо', 5)
stud3.rate_l(lect2, 'Письмо', 2)
stud3.rate_l(lect2, 'Математика', 6)

print(stud1)
print()
print(stud2)
print()
print(stud3)
print()
print(rev)
print()
print(rev2)
print()
print(lect1)
print()
print(lect2)
print()
var = stud1 < stud2
print()

list_of_student = [stud1, stud3]
print('Cредняя оценка за домашние задания по всем студентам в рамках курса',
      avg_grades_hw_course(list_of_student, 'Математика'))

list_of_lecturer = [lect1, lect2]
print('Cредняя оценка за лекции всех лекторов в рамках курса', avg_grades_lect_course(list_of_lecturer, 'Математика'))
