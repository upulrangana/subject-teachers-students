from student import Student


class Teacher(object):
    student_list = []

    def __init__(self, teacher_name, teacher_subject):
        self.teacher_name = teacher_name
        self.teacher_subject = teacher_subject

    def teacher_info(self):
        print(f"Teacher Name  - {self.teacher_name}  Teacher Subject  -{self.teacher_subject} ")

    def create_student(self, name, subject):
        obj = Student(name, subject)
        self.student_list.append(obj)

    def student_print(self):
        for index, item in enumerate(self.student_list):
            print(f"Student Name  - {item.student_name}  Student Grade  -{item.student_subject}")
