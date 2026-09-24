class Student:
    pass

s1=Student()
s2=Student()

s1.name="daniel"
s1.id="dcl07"
s1.height=168
print(s1.__dict__)
print(s1.name,s1.id,s1.height)

#modifying
s1.name="abin"
s1.id="dcl09"
s1.height=423
print(s1.__dict__)
print(s1.name,s1.id,s1.height)
#------------------------------------------------------------
#second instance
s2.name="jose"
s2.id="dcl05"
s2.height=163
print(s2.__dict__)
print(s2.name,s2.id,s2.height)

#modifying
s2.name="abin"
s2.id="dcl09"
s2.height=423
print(s2.__dict__)
print(s2.name,s2.id,s2.height)

