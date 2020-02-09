class Student(object):
    def __init__(self, student_name, student_subject):
        self.student_name = student_name
        self.student_subject = student_subject

    def student_info(self):
        print(f"Student Name  - {self.student_name}  Student Grade  -{self.student_subject}")
