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



        
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python'] + ['Git']
some_student.finished_courses += ['Введение в программирование']

some_mentor = Mentor('Some', 'Buddy')
some_mentor.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.8)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_lecturer.rate_student(some_student, 'Python', 10)
some_lecturer.rate_student(some_student, 'Python', 9.8)
some_lecturer.rate_student(some_student, 'Git', 10)

print(some_student)
print(some_lecturer)
print(some_reviewer)
