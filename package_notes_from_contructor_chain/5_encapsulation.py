'''
Encapsulation:
    the process of protecting data by making the variable private and controlling
    their access through public setter and getter methods.

    or

    -bundling/wrappping data and methods together and protecting data from outside
     access.
    -direct access is not given to sensitive data, But the class shud control
     how the data is read/modified

     Steps to achieve Encapsulation:
     1)A class should be oublic non abstract class.
     2)define private variables
     3)have piblic setter method(to update the data with validation logic)
     4)have public getter method(to access/ read data saafety)

     NOTE:
     setter method:
         -used to modify private data
         -usually expected to take 1 parameter
         -validation logic shud be present inside ti
         -not supposed to return any value

     getter method:
         -used to access private data
         -usually does not take any parameter
         -supposed to return any value

     SYNTAX:
         class ClassName:
             def __init__(self):
                 self.__var=name  #private IV
                 
             def set_var(self,newvalue):
                 #validation logic
                 self.__var=newvalue

             def get_var(self):  #public getter method
                 return self.__var

         obj=CLassName()
         obj.set_var("newvalue")  #calling setter method
         print(obj.get_var()) #calling getter method

'''
