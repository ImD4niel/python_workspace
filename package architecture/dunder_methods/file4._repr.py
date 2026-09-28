class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author

    def __repr__(self):
        return "repr custom string"


b1=Book("math","anbnin")
print(b1)
print(repr(b1))
print()