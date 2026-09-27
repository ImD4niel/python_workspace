class Employee(object):
    def __init__(self,ename,esalary,edept):
        self.name=ename
        self.salary=esalary
        self.dept=edept

    def __str__(self):
        return f"{self.name}--->{self.salary}--->{self.dept}"


e=Employee("abin",32523,"chem")
print(e.__str__())