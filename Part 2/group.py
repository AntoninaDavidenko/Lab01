class Student:

    def __init__(self, name, surname, record_book, grades):
        self.name = name
        self.surname = surname
        self.record_book = record_book
        self.grades = grades


class Group:

    students = []

    def add_student(self, student):
        if len(self.students) <= 20 and self.check_student_name(student):
            self.students.append(student)

    def check_student_name(self, student):
        for student_ex in self.students:
            if student_ex.name == student.name and student_ex.surname == student.surname:
                print("Student already in class")
                return False
        return True

    def average(self):
        average_dic = {}
        for student in self.students:
            total = 0
            average = 0
            for grade in student.grades:
                total += grade
                average = total / len(student.grades)
            average_dic[f'{student.name} {student.surname}'] = average
        sorted_list = sorted(average_dic.items(), key=lambda x:x[1])
        print(sorted_list[-5:])


A_one = Group()
Karen = Student('Karen', 'Autukas', 1, [4, 5, 6, 2, 1])
Kimi = Student('Kimi', 'Ami', 2, [4, 5, 6, 4, 8])
Adam = Student('Adam', 'Smit', 2, [5, 5, 6, 4, 8])
Richard = Student('Richard', 'Jonson', 2, [4, 5, 1, 4, 8])
Mark = Student('Mark', 'Holder', 2, [4, 5, 6, 8, 8])
Andrew = Student('Andrew', 'Spenser', 2, [4, 5, 8, 8, 8])
A_one.add_student(Karen)
A_one.add_student(Kimi)
A_one.add_student(Adam)
A_one.add_student(Richard)
A_one.add_student(Mark)
A_one.add_student(Andrew)
A_one.add_student(Mark)
A_one.average()
