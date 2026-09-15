'''
d1={}
print(type(d1))
print(d1)

d2={1:100, 2:200, 3:300}
print(type(d2))
print(d2)

#key based not indexed based
print(d2[1])


d2={1:100, 2:200, 3j:300, False: 400}
print(type(d2))
print(d2)

#keys cannot be duplicated(if duplicated present then the last value will be displayed
d2={1:100, 2:200.99, 1:300-5j, 1: True}
print(type(d2))
print(d2)

#values can be duplicated 
d2={1:100, 2:100, 3:100, 4: 100}
print(type(d2))
print(d2)

#syntax to modify a value of dict
#ref_var[key]=new_value
d2={1:100, 2:100, 3:100, 4: 100}
print(type(d2))
print(d2)

d2[3]=500
print(d2)
'''

#methods of dictionary
#dict_methods

d1={}
d1[29]=200
d1[70]=56
print(d1)
#syntax to modufy a value or add key value to dict
#if key is not present then it creates and if presents then it modifies

#1. ref.setdefault(key,optionalvalue)
#it adds the key with the given value into dict,
#but if the vakue is not given the default value null will be used

d2={}
d2.setdefault(10,100)
print(d2)


d2={}
d2.setdefault(10,100)
d2.setdefault(20)
print(d2)


#2. ref.update(dict_another)
#it copies and adds the items of tht dict into reference

d1.update(d2)
print(d1)

#3. ref.get(key)
#it returns the value for the key,
#but if the key is not there it returns None
d1.get(70)
print(d1.get(70))

#4. ref.pop(key)
#it removes entire items and returns the value

d1.pop(29)
print(d1)
'''
#if key is not present it raises key error
d1.pop(297)
print(d1)

'''
#5. pop_item- it doesnot take any parameter
# ref.pop_item

d1.popitem()
print(d1)

'''
d3={}
d3.popitem() keyerror
print(d3)
'''

#6. ref.clear()

d1.clear()
print(d1)


#7. ref.keys()
#it returen the list of keys
d3={1:100,2:200,3:300,4:400}
print(d3.keys())

#8. ref.values()
#it returns the list of values from the dict

print(d3.values())

#9. ref.items()
#it returns the list of items from the dict but in tuple
print(d3.items())




