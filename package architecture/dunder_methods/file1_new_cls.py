class Pen(object):
    def __init__(self):
        print("initialization")

#p=Pen()
p=Pen.__new__(Pen) #step1 : new pen created and returned
Pen.__init__(p)    #step2 : initialization code
