'''
object class:
    IN PYTHON every class automatically inherits from a built in class called
    object.
    -its the ultimate base class the root of python inheritance hierarchy.
    -even if you dont explicitly mention it, your classes inherit from object.

    -Importance of object class:
        the object clas provide a set of useful predefined special methods
        (dunder methods) that give "default behaviors to all objects", such
        as:
            -Printing/string representation
            -Comparison operations
            -hashing
            -Identity an type checking etc..

    -few important dunder methods are
        1).__new__(cls)
        2).__init__(self)
        3).__str__(self)
        4).__repr__(self)
        5).__hash__(self)
        6).__eq__(self,other)

    ----------------------------------------------------------------------
    1).__new__(cls):
        -it is used to create an actual instance of class.
        -it creates and returns the instance ans it is actually reponsible
         for instance creation.
        -it used object. __new__(cls) to allocate the memory location for
         the instance

         #eg:
             class Pen(object):
                 def __init__(self):
                     print("initialiser")

             p=Pen()---------------->(1)p=Pen.__new__(Pen) #empty pen instance
                        |                                  is created & return
                        |
                        |----------->(2)Pen.__init__(p) #constructor gets
                                                        executed.\


    2).__init__(self):
        -this methods gets automatically called only when we create an instance
         and is used to perform initialiser of instance.
        -to define initialiser in custom class, we need to have self as 1st
         implicit parameter.

    3).__str__(self):
        -this method gets invoked whenever an instance is printed or when called
         str(objectref).
        -and when called, by default it returns the string representation of the
         instance.
        -string representation is FullyQualifiedClassName
        @hexadecimal format:
        -we can override the __str__() to return a custom string representation
         useful/understandable to user

         NOTE:__str__ must always return a string.

         class ClassName(object):   #inheritance  (1)
             def __str__(self):     #methodname para same (2)
                 return "custom string"  #change the implementation (3)

         SYNTAX:
             def __str__(self):


    4).__repr__(self)
        -this method returns unambiguous(not confusing) developer representation
         of an object.
        -is used to define how an object should be represented as a string,
         mainly for developers during debugging, logging and development.
        -this method gets called
            1)when __str__() is absent and __repr__() is defined and when an
             instance is printed
            2)when we invoke repr(objectref)
            3)when we print containers(collection of objects)
        -and when called by default it returns the string representation of the
         instance (exactly samae as str).


    5).__hash__(self):
        -this methods gets invoked when we call hash(object) and bydefault
         returns a unique integer(hash value)
        -hash value of an object is used in set and dictionary for quick search
         ing and maintaining unique values(remove duplicates).
        -default behaviour is to return a unique integer for each ocject

    NOTE:
        __hash__() must always return int

    SYNTAX:
        def ClassName:
            def __init__(self):
                #initialization logic

            def __hash__(self):
            return uniqueinteger

        obj=ClassName()
        print(hash(obj)) #print(obj.__hash__())


    6).__eq__(self,other);
        -this method gets invoked/called when 2 instances are compared using
         == operator and by default it compares Identity (addresses) of 2
         instances, but NOT values.
        -But in order to compare the values of custominstance rather than its
         addresses, we need to OVERIDE __eq__()

         NOTE:
        -__eq__() is overidden for the INBUILT types(int,floats,list) etc
        -this method shud always return a boolean (TRUE/FLASE).

        SYNTAC:
            def ClassName:
                def __init__(self):
                    #initialization logic

                def __eq__(self,other):
                return boolean value

            obj1=ClassName()
            obj2=CLassName()
            print(obj1==obj2) #print(obj1.__eq__(obj2))

    
    isinstance(object,ClassName):
        -its a predefined function that checks whether the given object belongs
         to a particular class or not
        -it returns boolean (TRUE/FALSE).
            

    '''

