from teacher import Teacher


def start():
    teacher_list = []
    while True:
        # create
        create_who = input("Create student or teacher  -")
        if create_who == "teacher":
            teacher_name = input("Enter Teacher Name  -")
            teacher_subject = input("Enter Teacher Subject  -")
            teacher = Teacher(teacher_name, teacher_subject)
            teacher_list.append(teacher)
        if create_who == "student":
            student_name = input("Enter Student Name  -")
            student_subject = input("Enter Student subject  -")
            teacher.create_student(student_name, student_subject)
        # mechod
        method = input("Enter Your Method  -")

        if method == "printstudent":
            print(teacher.student_list)
            teacher.student_print()
        if method == "printteacher":
            print(teacher_list)
            print(f"Teacher Name  - {teacher.teacher_name}  Teacher Subject  -{teacher.teacher_subject} ")

        if method == "print_subject_student":
            subjt = input("Enter Subject")
            print(f"Subject {subjt}")
            for index, item in enumerate(teacher_list):
                if item.teacher_subject == subjt:
                    print(f"Teacher of this Subject =  {item.teacher_name}")
            for index, item in enumerate(teacher.student_list):
                if item.student_subject == subjt:
                    print(f"      student name = {item.student_name}     \n ")
        else:
            pass


start()
