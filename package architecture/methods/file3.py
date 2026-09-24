class Ornaments:
    def __init__(self,metal,price,grams):
        self.metal=metal
        self.price=price
        self.grams=grams

    def display_ornaments(self):  #accecsing of IVs using IM
        print(self.metal)
        print(self.price)
        print(self.grams)

    def change_price(self,newprice):
        self.price=newprice
        print("price changed")

    
        

o1=Ornaments("gold",342654,2103)
o2=Ornaments("silver",244445,432)
o3=Ornaments("iron",23535,324)

o1.display_ornaments()
o2.display_ornaments()
o3.display_ornaments()

o1.change_price=234
