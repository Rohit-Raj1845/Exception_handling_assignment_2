QUESTION:-1. Explain why we have to use the Exception class while creating a Custom Exception.
Note:- Here Exception class refers to the base class for all the exceptions.
In Python, the base class for all exceptions is the BaseException class, and it is recommended to use this class as the base for creating custom exceptions. Here's why using the BaseException class is important when creating custom exceptions:

1. Standardization: By inheriting from the BaseException class, you align your custom exception with the standard exception hierarchy in Python. This hierarchy provides a consistent structure for organizing and categorizing different types of exceptions. It allows for consistent exception handling and promotes code readability and maintainability.

2. Exception Handling: Python's exception handling mechanism revolves around catching and handling exceptions. When an exception is raised, Python looks for an appropriate exception handler to process the error. By using the BaseException class, your custom exception can be caught and handled using the same exception handling constructs (try, except, finally) that are used for built-in exceptions. This ensures that your custom exception integrates seamlessly with the existing exception handling infrastructure.

3. Compatibility: The BaseException class is compatible with the standard exception handling mechanisms and practices in Python. Libraries, frameworks, and tools that work with exceptions will recognize and handle your custom exception when it is derived from BaseException. This compatibility makes it easier to integrate your code with other components and leverage existing exception handling functionality.

4. Exception Attributes and Methods: The BaseException class provides a set of attributes and methods that are useful for handling and inspecting exceptions. For example, exceptions derived from BaseException have attributes like args (to store exception arguments) and with_traceback() (to associate a traceback with the exception). By using the BaseException class, you inherit these built-in functionalities, which can be useful for debugging, logging, or providing additional information about the exception.

5. Language Consistency: Using the BaseException class ensures that your custom exception follows the conventions and patterns established in the Python language. It makes your code more consistent with the wider Python ecosystem and helps other developers understand and work with your code more easily.



QUESTION:-2. Write a python program to print python Exception Hierarchy.
import inspect
def treeClass(cls, ind = 0): 
    print('_' * ind, cls.__name__)

    for i in cls.__subclasses__(): 
        treeClass(i, ind + 3)

print("Hierarchy for Built-in exceptions is : ")
inspect.getclasstree(inspect.getmro(BaseException))
treeClass(BaseException)        



QUESTION:-3. What errors are defined in the ArithmeticError class? Explain any two with an example.
1. ZeroDivisionError :- Mathematically, dividing an integer by zero is wrong, and that is the reason why python crashes the program and returns an error message.
For exmaple :-
try: 
    arithmetic = 5/0
    print(arithmetic)
except ZeroDivisionError as e: 
    print(e)    

2. OverFlowError :- An OverFlowError exception is raised when an arithmetic operation exceeds the limits to be represented. This is part of the ArithmeticError Exception class.
For example :- 
j = 5.0
for i in range(1,1000): 
    j = j**i
    print(j)



QUESTION:-4. Why LookupError class is used? Explain with an example keyError and IndexError.
LookupError Exception is the base class for errors raised when something can't be found.
The Python KeyError is an exception that occurs when an attempt is made to access an item in a dictionary that does not exist.
ages = {'A':45,'B':51,'C':67}
print(ages['A'])
print(ages['B'])
print(ages['C'])
print(ages['D'])

An IndexError means that Your code is trying to access an index that is invalid.
myList = [1,2,3,4,5,6,7,8,9,10]
print("The list is:",myList)
index = 10
element = myList[index]
print("Element at index {} is {}".format(index,element))



QUESTION:-5. Explain ImportError. What is ModuleNotFoundError?
ImportError occurs when the python program tries to import module which does not exist in the private table.
ModuleNotFoundError occurs when you're trying to access or use a module that cannot be found.



QUESTION:-6. List down some best practices for exception handling in python.
10 Python Exception Handling Best Practices:-

1. Use Exceptions for Exceptional Cases.
2. Don't Swallow the Exception.
3. Catch Specific Exceptions.
4. Always Clean Up Resources in a Finally Block.
5. Avoid Raising Generic Exceptions.
6. Raise Custom Exceptions.
7. Define Your Own Exception Hierarchy.
8. Document All Exceptions Thrown by a Function.
9. Provide Contextual Information When Raising an Exception.
10. Write Tests to Ensure That Exceptions Are Raised Correctly.
