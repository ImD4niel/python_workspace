class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

class Citizen(Person):
    def __init__(self,name,age,height,citizenid,nation,currency):
        super().__init__(name,age,height)
        self.citizenid=citizenid
        self.nation=nation
        self.currency=currency

class Refugee(Person):
    def __init__(self,name,age,height,refugeeid,origin,exitdate):
        super().__init__(name,age,height)
        self.refugeeid=refugeeid
        self.nation=origin
        self.currency=exitdate

c1=Citizen("dan",20,5.6,1234,"india","INR")
print(c1.__dict__)

r1=Refugee("john",25,6.0,5678,"syria","2023-12-31")
print(r1.__dict__)