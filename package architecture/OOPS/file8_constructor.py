class State:
    country="india"
    currency="rupee"
    president="pre"
    def __init__(self,name,lang,cap):
        self.name=name
        self.language=lang
        self.capital=cap

s1=State("Karnataka","Kannada","bengaluru")
s2=State("Kerala","malayalam","trivandrum")
s3=State("tamilnadu","tamil","chennai")

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

