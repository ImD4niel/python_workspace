class Student:
    def __init__(self, name, marks):
        self.name=name  #public IV
        self.__marks=marks  #private IV

    def parent_teachers_meet(self):  #public IM
        print("marks scored is",self.__marks)


s1=Student("daniel",34)
print(s1.name) #access public IV outside class
#print(s1.__marks) #access private IV outside the class
s1.parent_teachers_meet()