class Politician:
    def __init__(self,name,wealth):
        self.name=name
        self.__wealth=wealth

    def __raise_funds(self):
        print("politician raising funds")

    def ed_raid(self):
        self.__raise_funds()
        print(self.__wealth)

p1=Politician("trump",70000)
#print(p1.wealth)
#p1.__raise_funds()
p1.ed_raid()