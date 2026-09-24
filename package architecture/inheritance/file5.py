#hiracrcal
class Player:       #parent class
    def play(self):
        print("they are playing")


class CricketPlayer(Player):        #is a relation
    def bat(self):
        print("they are batting")

class FootballPlayer(Player):
    def goal_keeping(self):
        print("goal keeping")

class kabadiPlayer(Player):
    def raid(self):
        print("kabadi")

p=kabadiPlayer()        #initialization
p.raid()
p.play()
print(kabadiPlayer.__mro__)

q=FootballPlayer()        #initialization
q.goal_keeping()
q.play()
print(FootballPlayer.__mro__)
