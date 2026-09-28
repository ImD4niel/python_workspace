#print(5+4)
print((5).__add__(4)) #this is how python internally works, it calls the dunder method __add__ to add two numbers

#print(5-4)
print((5).__sub__(4)) #this is how python internally works, it calls the dunder method __sub__ to subtract two numbers

#print(5*4)
print((5).__mul__(4)) #this is how python internally works, it calls the dunder method __mul__ to multiply two numbers

#print(5/4)
print((5).__truediv__(4)) #this is how python internally works, it calls the dunder method __truediv__ to divide two numbers

#print(5//4)
print((5).__floordiv__(4))

#print(5%4)
print((5).__mod__(4))

#print(5**4)
print((5).__pow__(4))