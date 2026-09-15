'''
python architecture:
    -it explains how python executes our program within (.py) file into
     output.

     1.Source files(.py):
         program written in plain text(types character using keyword)
         
     2.lexical/tokenisation:
         -breaks the source code intp a sequence of tokens
         -tokens are individual unit of code(identifier,keyword,literal,
          operator,seprator)
          
     3.paring
         -checks if seq of tokens is gramatically valid or not
         -if valid->its builds AST(abstract syntax tree)
     4.Compilation:
         process of converting into AST into Bytecode
         ->cpython stores bytecode(.py files) inside folder names as _pycache_
         ->later it helps in faster loading on same machine and same python
          version
          
     5.module loading(import system):
         -during the execution/importing, module loader loads .py file
          or .pyc files and creates "code objects" in memory.
         -code obj=(compiled bytecode +metadatta) which os executed by PVM.
         
     6.PVM-python vertual machine:
         -executes engine that runs bytecode
         -and generates the output.
          
    python is platform indeppendent?
        the same .py file can be run on windows, linux, mac or android but
        they shud have installed python interpreter.

--------------------------------------------------------------------------------------
Package Attecture->explains how python files,folders are structed into a package

    MODULE->single .py file
          ->contains variables, function, classes
          ->represents a reusable unit of code

    2 types:
        -Inbuilt modules
        eg:keyword, math, random, os, json, pickle

        -Userdefined modules:
        eg:sample.py demo.py

----------------------------------------------------------------------------------
PACKAGE->
    A folder that contains multiple modules and it contains __init__.py

'''
