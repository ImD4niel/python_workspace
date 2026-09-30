class Park:
    authority = "GBA"      # public class variable, belongs to the class and not to any instance of the class
    def __init__(self, name,location):
        self.name = name                #instance variable, belongs to the instance of the class
        self.location=location          #instance variable, belongs to the instance of the class


    def open_park(self):        #public instance method, self is the instance of the class Park
        print("park opens on weekdays",self.name)  #access public Instanve vriable inside the class


    @classmethod
    def change_authority(cls,new_authority):  # public class method, cls is the class Park
        cls.authority = new_authority  #modify the public class variable inside the class


p1=Park("Zenpaark","bafa")
p1.open_park()  #access the public Instance method outside the class