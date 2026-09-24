class Employee:
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.salary=sal

e1=Employee("girish",32,40000)
e2=Employee("ramwsh",67,32050)
e3=Employee("suresh",25,64000)

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)