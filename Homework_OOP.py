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

    def __str__(self):
        if self.grades:
            average_grade = sum(sum(grade) / len(grade) for grade in
self.grades.values()) / len(self.grades)            
            return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {average_grade}\n \
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}"
        else:
            return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: 0.00 \n \
                 Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n Завершенные курсы: {', '.join(self.finished_courses)}"
        
        
    
             
 


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}\n Закрепленные курсы: {', '.join(self.courses_attached)}"   


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def rate_student(self, student, course, grade):   
        if isinstance(student, Student) and course in self.courses_attached:
            if course in self.grades_from_students:
                self.grades_from_students[course] += [grade]
            else:
                self.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__(self, other):
        if self.grades_from_students and other.grades_from_students:
            self_average = sum(sum(grade) / len(grade) for grade in self.grades_from_students.values()) / len(self.grades_from_students)
            other_average = sum(sum(grade) / len(grade) for grade in other.grades_from_students.values()) / len(other.grades_from_students)
            return self_average < other_average
        else:
            return False       
    
    def __str__(self):
        if self.grades_from_students:
            average_grade = sum(sum(grade) / len(grade) for grade in self.grades_from_students.values()) / len(self.grades_from_students)                             
            return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {average_grade}"
        else:
            return f"Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: 0.00"    


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f"Имя: {self.name}\n Фамилия: {self.surname}"  

def average_grade_on_the_course(student_list, course_name):
    total_grades = 0
    count_students = 0
    for student in student_list:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name]) / len(student.grades[course_name])
            count_students += 1
    if count_students == 0:
        return f"Средняя оценка всех студентов по курсу {course_name}: 0.00"
    else:
        average_grade = total_grades / count_students
        return f"Средняя оценка всех студентов по курсу {course_name}: {average_grade:.2f}"    

def average_grade_from_students(lecturers_list, attached_course):
    total_grades1 = 0
    count_lecturers = 0
    for lecturer in lecturers_list:
        if attached_course in lecturer.courses_attached:
            total_grades1 += sum(lecturer.grades_from_students[attached_course]) / len(lecturer.grades_from_students[attached_course])
            count_lecturers += 1
    if count_lecturers == 0:
        return f"Средняя оценка всех преподавателей по курсу {attached_course}: 0.00"
    else:
        lecturer_grade = total_grades1 / count_lecturers
        return f"Средняя оценка всех реподавателей по курсу {attached_course}: {lecturer_grade}"          

        
student1 = Student('Dmitriy', 'Bodryakov', 'man')
student1.courses_in_progress += ['Python'] + ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Daniil', 'Voskresenskiy', 'man')
student2.courses_in_progress += ['Python'] + ['Git']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Oleg', 'Buligyn')
lecturer1.courses_attached += ['Python'] + ['Git']

lecturer2 = Lecturer('Egor', 'Budancev')
lecturer2.courses_attached += ['Python'] +['Git']

reviewer1 = Reviewer('Igor', 'Karpov')
reviewer1.courses_attached += ['Python'] + ['Git']

reviewer2 = Reviewer('Anatoliy', 'Semenov')
reviewer2.courses_attached += ['Git'] + ['Python']

lecturer1.rate_student(student1, 'Python', 10)
lecturer1.rate_student(student1, 'Git', 9)

lecturer2.rate_student(student2, 'Python', 9)
lecturer2.rate_student(student2, 'Git', 10)

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 10)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 9)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
print(lecturer1 < lecturer2)
print(average_grade_on_the_course([student1, student2], 'Python'))
print(average_grade_on_the_course([student1, student2], 'Git'))
print(average_grade_from_students([lecturer1, lecturer2], 'Git'))
print(average_grade_from_students([lecturer1, lecturer2], 'Python'))