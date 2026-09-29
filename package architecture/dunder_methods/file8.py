class Money:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Money(self.value + other.value)
    
    def __sub__(self, other):
            return Money(self.value - other.value)

    def __mul__(self, other):
            return Money(self.value * other.value)

    def __truediv__(self, other):
            return Money(self.value / other.value)

    def __floordiv__(self, other):
            return Money(self.value // other.value)  

    def __mod__(self, other):
            return Money(self.value % other.value)

    def __pow__(self, other):
            return Money(self.value ** other.value)
    

    def __str__(self):
        return f"Money: {self.value}"



m1=Money(100)
m2=Money(200)
m3=Money(500)
print(m1+m2+m3) #this will call the __add__ method of Money class and return the sum of m1 and m2
print(m2+m3) #this will call the __add__ method of Money class and return the sum of m2 and m3
print(m1+m3) #this will call the __add__ method of Money class and return the sum of m1 and m3
print(m1-m2) #this will call the __sub__ method of Money class and return the difference of m1 and m2
print(m2-m3) #this will call the __sub__ method of Money class and return the difference of m2 and m3
print(m1-m3) #this will call the __sub__ method of Money class and return the difference of m1 and m3
print(m1*m2) #this will call the __mul__ method of Money class and return the product of m1 and m2
print(m2*m3) #this will call the __mul__ method of Money class and  return the product of m2 and m3
print(m1/m2) #this will call the __truediv__ method of Money class and return the division of m1 and m2
print(m2/m3) #this will call the __truediv__ method of Money class and return the division of m2 and m3
print(m1//m2) #this will call the __floordiv__ method of Money class and return the floor division of m1 and m2
print(m2//m3) #this will call the __floordiv__ method of Money class and return the floor division of m2 and m3
print(m1%m2) #this will call the __mod__ method of Money class and return the modulus of m1 and m2
print(m2%m3) #this will call the __mod__ method of Money class and return the modulus of m2 and m3
print(m1**m2) #this will call the __pow__ method of Money class and return the power of m1 and m2
print(m2**m3) #this will call the __pow__ method of Money class and return the power of m2 and m3