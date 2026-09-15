'''it is a predefined class in python
   ' ', " ", ''' '''
'''
'''
s='sagar'
print(s)

s2=str()
print(s2)
print(type(s2))
#string is a indexed based collecetrion


s3="python"
print(s3[-1])
'''

#methods fo string
s1="python is good"
#1) ref.capitalize()
#it returns the copy of the string where only the 1st letter will capitalize
print(s1.capitalize())

#2)ref.title()
#it returns a copy of a string whrer 1st letter of each word is capitalized
print(s1.title())

#3) ref.upper()
#it returns the copy of string in uppercase form
print(s1.upper())

#4 ref.lower()
#it returns the copy of string in lowercase
print(s1.lower())


#5) ref.isupper()
#it checks whether the string is in uppercase or not
#it returns true if the strings which is in uppercased string
print(s1.isupper())

#6) ref.islower()
#it checks whether the string is in lower or not
#it returns true if the strings which is in ulowercased string
print(s1.islower())

#7) ref.startswith("substring")
#it returns true if the string starts with the given substring.
s2="Abin Joseph"
print(s2.startswith("Abin"))

#8) ref.endswith("substring")
#it returns true if  string endswith the given substring
print(s2.endswith("eph"))

#9) ref.replace("oldstring","newsubstring")
print(s2.replace("Abi","gub"))

#10) ref.isalpha()
#it returns true if the string contains only alphabets(upper or lower)
s3="J0seph"
print(s3.isalpha())

#11) ref.isdigit()
#it returns true if the string contains only digits
s4="8468412759"
print(s4.isdigit())

#12) ref.isalnum()
#it returns true is string contains either alphabets or digit or both, no spacc
s5="Joseph 2"
print(s5.isalnum())

#13) ref.swapcase()
#it returns the copy of string where uppercase letters are swaped with loer case
#and viseversa

s6="abIn"
print(s6.swapcase())

#14) ref.count("substring")
#it returns the number of occuraNces of the substring
s7="malayalam"
print(s7.count("a"))



#15) ref.index("substring")
#it returns thw index number of the 1st occuranging substring
s8="prestige"
print(s8.index("e"))

#16) ref.lstrip()
#it returns the copy of a string with leading/left-hand-side spaces removed
s9="  BOOM"
print(s9.lstrip())

#17) ref.rstrip()
#it returns the copy of a string with trailing/right-hand-side spaces removed
s10="BOOM  "
print(s10.rstrip())

#18) ref.strip()
#it returns a copy of strong with bith leading/trailiong spaces remoived
s11="  BO OM  "
print(s11.strip())


#19) ref.split()
#it slipts the strings based on space as a seperetor and returns list
#of substrings
s12="dhee coding space"
print(s12.split())

s13="7/8/2026"
print(s13.split("/"))


#20) "substring".join(listofstrings)
#it returns a copy of a string with the substring joined btw those strings
#concatanation
dates=["15","08","1947"]
print("/".join(dates))


s=" Today is Friday Good Afternoon "
print(len(s.split()))
s1=s.split()
print(s1[2])









