def workingWith():
    #simple lambda functions 
    #A lambda function is a small anonymous function, A lambda function can take any number of arguments, but can only have one expression.
    #lambda args : expressions
    #lambda function can be used wherever function objects are required.
    #lambda functions can be used to pass a function as an argument.
    #lambda functions can be used wherever function objects are required.
    #The power of lambda is better shown when you use them as an anonymous function inside another function.
    """
    why use lambda
    Say you have a function definition that takes one argument, and that argument will be
    multiplied with an unknown number:
    """
    x = lambda a, b : a + b
    print(x(4,6))

workingWith()

def anonymousfunc(n):
    return 