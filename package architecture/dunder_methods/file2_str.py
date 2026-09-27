class Pen(object):
    def __init__(self,color,cost,brand):
        self.color=color
        self.cost=cost
        self.brand=brand
        print("initialization")

    def __str__(self):  #step2
        return f"{self.cost}-->{self.color}-->{self.brand}"  #step3

p=Pen("red",54,"dsf")
#print(p)  #gives address
print(p.__str__())  #gives adreess in background of print(p)


