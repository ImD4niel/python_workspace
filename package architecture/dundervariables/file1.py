#print(type(__name__),__name__)
#if we execute a module containing __name__ direactly using python -m package.module
#__name__=="__main__"
#print(__name__=='__main__')


def add(a,b):
    print(a+b)

if __name__=="__main__":
    add(10,20)