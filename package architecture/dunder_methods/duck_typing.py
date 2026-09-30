class Zomato:
    def deliver(self):
        print("zomato delivers")

class Swiggy:
    def deliver(self):
        print("swiggy delivers")

class Swish:
    def deliver(self):
        print("swish delivers")


class Rapido:
    def commute(self):
        print("rapido commutes")

def process_delivery(partner):
    if hasattr(partner,"deliver"):  #safe duck typing, check if the partner has deliver method or not. 
        partner.deliver()


z=Zomato()
s=Swiggy()
sh=Swish()
r=Rapido()
l=[z,s,sh,r]

for p in l:
    process_delivery(p)
print(hasattr(z,"deliver")) # True
print(hasattr(z,"commute")) #is commute method present in zomato class? False
print(hasattr(r,"commute")) #is commute method present in rapido class? True
