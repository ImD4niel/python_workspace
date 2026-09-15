
b=True
i=10
f=2.5
c=1+2j

#impliicit type casting
#b -> i -> f -> c

b_i=b+i
print(b_i)
print(type(b_i))

b_f=b+f
print(b_f) 
print(type(b_f))

b_c=b+c
print(b_c)
print(type(b_c))

i_f=i+f
print(i_f)
print(type(i_f))

i_c=b+c
print(i_c)
print(type(i_c))
'''
#EXPLICIT TYPECASTING
'''
i_f=float(i)
print(i_f)
print(type(i_f))

i_c=complex(i)
print(i_c)
print(type(i_c))


b_i=int(b)
print(b_i)
print(type(b_i))

b_f=float(b)
print(b_f)
print(type(b_f))


b_c=complex(b)
print(b_c)
print(type(b_c))


b_i=bool(i)
print(b_i)
print(type(b_i))

#typecasting among multiple value datatype
l=[10,20,30]
t=(21,31,41)
s={11,22,33}
st='abc'
d={1:20,2:20,3:30}

print(tuple(l))

print(set(l))

print(str(l))

#print(dict(l))

#--------------------
print(list(t))
print(set(t))
print(str(t))
#print(dict(t))

#---------------

print(list(s))
print(tuple(s))
print(str(s))
#print(dict(s))
#----------------


print(list(st))
print(tuple(st))
print(set(st))
#print(dict(st))


#--------------

print(list(d))
print(tuple(d))
print(set(d))
print(str(s))
'''
#------------------------------------------------------------------------
#convert single valued to multivalued
#class 2
b=True
i=10
f=1.2
c=5+7j
print(str(b))
print(type(str(b)))

print(str(i))
print(type(str(i)))

print(str(f))
print(type(str(f)))

print(str(c))
print(type(str(c)))

#-----------------------------------
print("-------------------------")
l=[10,20]
t=(23,33)
s=(11,22)
st="python"
d={'a':100,'b':200}

print(bool(l))
print(bool(t))
print(bool(s))
print(bool(st))
print(bool(d))

#all default values are falsy value
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(""))
print(bool(dict()))

#convert the string to int
sti='10'#parsing: converting a string into its -
        #- corresponding single valued datatype explicitly is known as parsing
print(int(sti))
print(type(int(sti)))

#convert the string to float
#st2="two.one"#if 2.1 is writen then it wont show error
#print(float(st2))


#
st3="3.2j"
print(complex(st3))



#character conversion
#it means changing a character into its numeric value and vise-versa.
#python internally represents every character by "Unicode Code point(uniqie number assigend to every character)"
#character converstion is a form of single valued typecating.

two impoetant funtion with respect tot character converstion.
1. ord('character')
it is a funtion which returns a unicode integer for that given character.
2. chr(unicode integer)
it is funtion which returns the character corresponding to the given unicode number.
'''









