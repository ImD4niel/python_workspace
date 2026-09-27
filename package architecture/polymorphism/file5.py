#hirarchical, overriding, super() concept
from typing_extensions import override


class Person:
    def register(self,name):
        print("person shud register as per the government",name)

class Employee(Person):
    @override
    def register(self,name):
        super().register(name)
        print("employees are reg as per EPFO",name)

class Student(Person):
    @override
    def register(self,name):
        super().register(name)
        print("student reg as per the board",name)

e=Employee()
e.register("sf")
print("------")
s=Student()
s.register("dan")



        