class Product:
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price


    def __hash__(self):
        return self.pid 
    
p1=Product(101, "laptop", 50000)
print(hash(p1))
p2=Product(102, "mobile", 20000)
print(hash(p2))