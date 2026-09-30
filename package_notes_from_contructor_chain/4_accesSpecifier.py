'''
acess specifier:
    -it applies only inside classes, a because classes are about encapsulation
    -these are used to specify the visibility or accessibility of variables
     or method.

     3 TYPEs:
     1).public
     2).protected
     3).private



    1).public:
        -any var or method declore normally inside a class is by default
         considered as public
        -no leading underscore are used for it
        -such var or methods can be accessed from anywhere(from inside class
         or from outside class in samemodule or module in samepackage).


    2).Protected:
        -any var or method declared using "single leading underscore" inside
         a class is considered as protected
        -protected is meant for internal usage by child class
        -it shud be used either in same class or its child classes and this
         is convention not an enforcement.


    3).private:
        -any var or method declared using "double leading underscore" inside
         a class considered as private.
        -private cannot be accessed directly from outside the class, it can
         be accessed only from inside the class using methods.
        -used specially to hide sensitive data.
         


'''
