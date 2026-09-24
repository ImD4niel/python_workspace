class Student:

    @staticmethod
    def calculate_percentage(marks,total_marks):
        return (marks/total_marks)*100



print(Student.calculate_percentage(63,270))#access the SM using calculator

s1=Student()
print(s1.calculate_percentage(572,625))


