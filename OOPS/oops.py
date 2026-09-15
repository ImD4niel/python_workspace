'''
OPPS:
    in python we can write program without class,but real time large scale
    project oops


    -object oriented:
        -represented everything in prog in the form of object that strores
         data(states) and perform action(behaviours)
        -python treats almost everything as an object (numners,str,list,func etc


    -class:
        -blueprint/logicalentity(template),that describes the property and
         behavior of an object
        -class define states represented using variables
        -behaviour represents using methods

    SYNTAX for userdefined class->
        class ClassName:
            pass

    -Object:
        -instance of a class
        -it repre real world(student,employee,account) or logical entity(
         int,lsit,str,obj) that has state nd behaviour instantiation
        -process of creating instance of a class
        -notes:
            to create an object,class must be created first
        -syntax:
            instancereference=ClassName()

        -using one class-> we can create multiple instanve and each instance is
         independent entity
        -changes made to 1 instance does not affect other instances.
    -----------------------------------------------------------

    MEMORY ALLOCATION wrt CLASS and INSTANCES
        -when class is defined, class dictionary gets created and inside it
         variables and ,ethods of that class is stored in the form of key and
         values.

        -when instance is created, instance dictionary gets created and inside
         it instance data is stored in the form of key and values,
         it will have a refernce to class.

        NOTES:
            print(ClassName.__dict__) #display the class dictionary
            print(objrefernce.__dict__) #display the instance dictionary
'''
