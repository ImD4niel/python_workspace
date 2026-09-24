class Student:
    school_name='adfhatjq'
    principal="dfhdw"
    location="in"

    def __init__(self,name):
        self.name=name

    @classmethod
    def display_school_details(cls):
        print(cls.school_name)
        print(cls.principal)
        print(cls.location)

    @classmethod
    def change_principal(cls,new_princi):
        cls.principal=new_princi



Student.display_school_details()
Student.change_principal("abin")
print(Student.principal)
