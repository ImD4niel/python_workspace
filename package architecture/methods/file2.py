class State:
    president="A"
    currency="rupee"


    @classmethod
    def display_country(cls):
        print(cls.president)
        print(cls.currency)

    @classmethod
    def elect_president(cls,new_president):
        cls.president=new_president


State.display_country()
State.elect_president("B")
print(State.president)