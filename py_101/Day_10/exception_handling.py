'''
Error occurs while code execution, we call it exception in python ....will stop the execution and generate error message.
To handle this errors/exception we use:
    - try: it allows you to test a block of code for errors
    - except: it allows you to handle the error
    - else: lets you execute code when there is no error
    - finally: regardless of errors or not, this executes the code

Some common exception in Python are:
    1. NameError: when variable is not defined
    2. IndexError: when index is not found in sequence
    3. ImportError: when an import statement fails
    4 . .....please check documentation 
'''

#handle import error
try:
    import sample_module
except ImportError:
    print("No such module you have! Don't smoke and write code!")

# handle name error
try:
    print(ananya_hungry) #gives error
except NameError:
    print('Error occured!\nWho is ananya?')

# handle index error
list_ex = [1,2,3,4,5,6,7]
'''
suppose I'm high and trying to access 7th element list_ex[7] what will I get? 

IndexError because indexing starts from 0 and goes till n-1 {n: number of elements}
'''
try:
    print(list_ex[7])
except IndexError:
    print("YOLO! You only code once before you get fired")


# All errors
dict_ex ={
    "name": "Ravi",
    "age": "72",
    "married": "NO"
}

try:
    print(dict_ex['job'])
except: # key block gives you KeyError, when you don't mention what kind of error to handle in except..it handles every error generated in try block.
    print("You have no such key!")

# Handle exception with appropriate message then we need to catch the exceptions.

try:
    print(dict_ex['job'])
except Exception as error:
    print(f"An error occurred: {error=}, {type(error)=}" ) #gives you what error occured, and type of error

'''
note: Catching all Exception can cause issue, when you want to raise an issue in some usecase...so be careful and mention properly what exception you want to catch.
'''

ananya_hungry = True
# multiple exception
try:
    print('=============')
    print(dict_ex['age'])
    print(list_ex[6]) 
    print(ananya_hungry) 
except(NameError, IndexError, KeyError) as e:
    print(f"Error occured: {e=}")
else: # when no exception is raised and else block will be executed
    print("NO error Occured!")
finally: #regardless of error or not this block will be executed
    print("Play around with try block to see different errors")

'''
Difference between finally and else is that 

'else' block will be executed only if no exception is raised, but
'finally' block will be always executed
'''

