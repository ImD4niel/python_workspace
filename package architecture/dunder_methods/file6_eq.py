class Car:
    def __init__(self, modelno, price):
        self.modelno = modelno
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Car): #if it is of car type, compare or else direct comparison will not work
            return self.modelno == other.modelno #content comparison
        else:
            return False
        
c1=Car(34,50000)
c2=Car(45,50000)
print(c1==c2)
#print(isinstance(c2,Car))