'''
GENERATOR:

    -it is a function that is used to create a custom sequence of elements
     using the "yield" keyword.
    -if a user-defined function contains at least one yield keyword, then that
     function becomes a generator function.
    -gerenerator generate values one-by-one (not all at once).
    -generators are mainly used to create custom sequence (like even numbers,
     fibinocci,primes, inifinite sequence, odd number, large data strems).
    =>generator object is created ONLY ONCE, when the "function containing
     YIELD keyword" is called.
    =>each yield returns ONE value, when next() or for loop asks for it.

    Yield:
        when python executes yield:

        1.it returns the yielded value to the caller.
        2.it pauses the function (remember variables and the next line).
        3.when you call next() again, it "resumes right after yield".
        4.automatically creates an iterator.

        EXAMPLE:
        1.
        def fun():
            yield(10)
            yield(20)
            yield(30)

        gen_obj=fun()  #1.when u call genfunction it returns genobj and this genobj is an iterator.
        print(next(gen_obj)) #output: 10
        print(next(gen_obj)) #output: 20
        print(next(gen_obj)) #output: 30
        print(next(gen_obj)) #error: stopiteration because 

        2.
        def fun():
            value=0
            yield(value)
            value=value+1
            yield(value)
            value=value+2
            yield(value**2)
            value=value+3
            yield(value**3)
            value=value-2
            yield(value**2)
            
        gen_obj=fun()  #1.when u call genfunction it returns genobj and this genobj
                       #is an iterator.
        print(next(gen_obj)) #output: 0
        print(next(gen_obj)) #output: 1
        print(next(gen_obj)) #output: 9
        print(next(gen_obj)) #output: 216
        print(next(gen_obj)) #output: 16


        3.
        def fun():
            value=0
            yield(value)
            value=value+1
            yield(value)
            value=value+2
            yield(value**2)
            value=value+3
            yield(value**3)
            value=value-2
            yield(value**2)
                    
        gen_obj=fun()  #1.when u call genfunction it returns genobj and this genobj
                               #is an iterator.
        for i in gen_obj:
            print(i)


=========================================================================================
==========================================================================================
#LAMBDA FUNCTION:
    -this function is small, anonymous function defined using lambda keyword.
        or
    -A lambda function is a function without a name, written in a single line, and used for
     short operations.
    -return shoud not be used
    NOTE:
        -LAMBDA function is best "when we need to pass simple helper function" for higher
         order function(function which takes other function as a parameter.)

        Syntax of lambda:
        lambda parameter:expression

    key rules:
        -no function name
        -no return keyword
        -expression result is returned automatically


    EXAMPLE:
    1.
    lambda a,b: a+b
'''

v=lambda a,b: a+b
print(v(1,2))

w=lambda n:n**2
print(w(2))

e=lambda a,b,c,d:a+b-c+d
print(e(10,5,20,15))
'''





