#eval
'''
eval
-it is an built in funtion thaat evalutes the strringa as a pythin expression and returns
the result.
-it can automatically decides the type

expression: it is any valid combination of values, variables, operators, and funtions,
that produces a single value when evaluated or calculated

result = eval("expression within a string")
'''

res=eval("2+5")
print(res)

a=100
b=25
res1=eval("a-b+50")
print(res1)


l=[10,20,30]
res3=eval("len(l)+24")
print(res3)

print(eval("[]"))


print(eval("(10,20,30)"))

print(eval("{1:20,2:30,3:40}"))

print(eval("False"))
#automatically typscasting and useful for accepting boolean value
#from user and evluating expressions.


