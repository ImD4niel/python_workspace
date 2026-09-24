'''

    -SYNTAX to create list comprehension:
            l1=[expression for variable in sequence]

    1.
        nl=[i+10 for i in [2,3,4,5,6]]
        print(nl) #output:[12,13,14,15,16]

        print(list(map(lambda i:i+10,[2,3,4,5,6])))

    2.
        nl=[i**3 for i in [2,3,4,5,6]]
        print(nl)


        ol=["Amy","Ben","Chad","Divya","Evan"]
        nl=[len(i) for i in ol]
        print(nl)

    -2nd SYNTAX to create list compreshension

        l2=
    ==============================================================================
    =
    ==============================================================================
    ==============================================================================
    =

ol={2:10,3:20,4:30,5:40,6:50}
print({i:(ol[i]**2 if i%2==0 else ol[i]**3) for i in ol})
            #OR     #using uppacking
print({k:(v**2 if k%2==0 else v**3) for k,v in ol.items()})

============================================================================================
    zip function:
        -IT IS A PREDedined function in python that combines multiple iterables elements
         by elements.
        -it creates tuples of corresponding elements from each iterable
        -zip function accepts two or more iterables and returns zip object(iterators).

        SYNTAX:
            -zip_obj=zip(iterable1,iterables2,..)
            
            Note:1.each elements inside zipobject is a tuple.
                 2.zip object stops at the shortest iterable.
                 3.it is used for mapping and pairing.

         Example:
            1.
            rolls=[32,40,60,33]
            names=['Amy','Ben','chad','Denzo']

            print(list(zip(rolls,names)))
            #output:[(32, 'Amy'), (40, 'Ben'), (60, 'chad'), (33, 'Denzo')]
        
       2.
            rolls=[32,40,60,33,21,23,28,34]
            names=['Amy','Ben','chad','Denzo']

            print(list(zip(rolls,names)))
            #OUTPUt:[(32, 'Amy'), (40, 'Ben'), (60, 'chad'), (33, 'Denzo')]

            3.
            rolls=[2,3,4,5,6,7]
            marks=[70,65,90,50,25,95]

            a=dict(zip(rolls,marks))
            print({k:("pass" if v<35 else "fail") for k,v in a.items()})
            #output:{2: 'fail', 3: 'fail', 4: 'fail', 5: 'fail', 6: 'pass', 7: 'fail'}



'''
rolls=[2,3,4,5,6,7]
marks=[70,65,90,50,25,95]

a=zip(rolls,marks)
print({k:("pass" if v<35 else "fail") for k,v in a.items()})




