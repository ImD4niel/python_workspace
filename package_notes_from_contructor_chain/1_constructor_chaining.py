'''
constructor chaing:
    it is the process where in parent class constructor is invoked/called
    from child class constructor using super()

    NOTE:
    1.super().__init__() is used to "reuse/restore the common initialization
     logic of the parent constructor/initialization from the child
     constructor, whixh reduces repetation od code ans thisis called as \
     constructor chainging

    2.Defining a constructor (__init__) in a child class will STOP the parent
    class constructor from being automatically called. the parent class
    attributes wont be initialization unless you "explicitly call super()"
    __init__() from the child constructor.

    3.super() doesnt just call the immedite parent, it follows the "method
    Resolution Order (MRO) in inheritence hierarchies, especially important
    in multiple inheritence.
    
    Syntax:
        class ParentClass:
            def __init__(self):
                #parent initialization logic     #1

        class ChildClass(ParentClass):
            def __init__(self):
                super().__init__():
                #child initialization logic      #2

        c=ChildClass()

        example:
        class ParentClass:
            def __init__(self,a,b):   #if prt_cnstrct is havinh n para
                #parent initialization logic     #1

        class ChildClass(ParentClass):
            def __init__(self,a,b):
                super().__init__(a,b): #whle cllg super() in chldcls pass n-1 argt
                #child initialization logic      #2

        c=ChildClass(10,20)
            
    
