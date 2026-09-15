from calculation.addition import add
from calculation.multiplication import multiply
def squarearea(side):
    print(multiply(side,side)) 

def squareperimeter(side):
    print(2*(add(side,side)))

squarearea(10)
squareperimeter(20)