#multiple inheritence
class Batsman:  #parent class
    def bat(self):
        print("they are batting")

class Bowler:   #parent class
    def bowl(self):
        print("bowling")

class AllRounder(Batsman,Bowler):   #childclass
    def field(self):
        print("allrounder")

q=AllRounder()  #intantiation
q.bat()
q.bowl()
q.field()
print(AllRounder.__mro__)