from typing_extensions import override
class Student:
    def study(self):
        print("student is studing")


class MedicalStudent(Student):
    @override
    def study(self):
        super().study()
        print("studing in library")

q=MedicalStudent()
q.study()

