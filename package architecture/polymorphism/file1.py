from typing_extensions import override

class Chef:             #parent class
    def cook(self):
        print("chef cooks")


class ItalainChef(Chef):  
    @override        #child class
    def cook(self):     #step2:method name shud be same as the parent method
        print("itialian flavour")   #step3:implementation in child method shouid be different

q=ItalainChef() #instantion
q.cook()