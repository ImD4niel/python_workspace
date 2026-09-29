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
    partner.deliver()


z=Zomato()
s=Swiggy()
sh=Swish()
r=Rapido()
l=[z,s,sh,r]

for p in l:
    process_delivery(p)