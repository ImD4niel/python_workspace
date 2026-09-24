class Student:
    course="pfs"
    roomnumber=101

Student.institute="DCL"
print(Student.__dict__)
print(Student.course)           #accesing syntax
print(Student.roomnumber)
print(Student.institute)
Student.institute="Dhee Coding Lab"  #modify syntax
print(Student.institute)
