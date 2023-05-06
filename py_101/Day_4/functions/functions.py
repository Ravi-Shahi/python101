'''
So Far, we learned lots of python Keywords & statements like
    - print
    - variables
    - control statement
    - decision statements

Today, we are going to learn about functions....Really Really Cool Topic

Suppose we write 15 lines of python statement for doing a particular task in our project ,
after writing 60-70 lines, we again require that particular task to writen in our project.... 

what do we do?

copy paste the 15 lines of code again and make our code look messy and cool?

No! repeating is not out style....we belive in energy conservation and for that we'll use something called "function"

A Function is just a labeled sack of python statement to perform a particular task. NOT kidding! let's see

'''

# code without function to write table of 2 and 3

# table 2

for num in range(1,11):
    print(2," * ",num," = ", num*2)
else:
    print("")

# table 3
for num in range(1,11):
    print(3," * ",num," = ", num*3)
else:
    print("")

'''
In above statement, we are repeating exact same loop and logic with minor changes
let's understand functions,

syntax:
def functionname(parameter):    
    statement(s)


    
--calling function is just
syntax:
    functionname(argument)

Note: parameter can be empty, if we don't need any values for our block of code \_/
'''

#empty_parameter function (direction to milk store)

def direct_to_store():
    print("from sector 15 station go towards momo-popo")
    print("take left")
    print("you'll see, kuku book store..turn right")
    print("There on your left, Milk Store :)")

direct_to_store()

def table(usr_num):
    for num in range(1,11):
        print(usr_num," * ",num," = ", num*usr_num)
    else:
        print("")

# numbers of table just by one line, this magic is called function 
table(5)
table(11)
table(12)

'''
parameter: defined in function defination (is just a placeholder)
    def functionname (i_am_parameter):
    
argument: this is actual value passed to function 
    functionname(4)


Types of Arguments:
    - Required: absolute to pass argument to a function
    - Keyword: pass argument to a function by parameter name
    - Default: if no argument pass, parameter will have a value as backup :)
    - Variable-length arguments:  (number of argument passed is not defined --> use asterisk(*))
'''

# Required Argument
def required_arg(word_please):
    print('This is must:',word_please)


# calling required_arg() ---> calling like this will give error, must pass a value
required_arg("This string is argument")

# Keyword Argument
def keyword_arg(name,order):
    print(f"{name}'s order is: {order}")


keyword_arg(name='Ravi',order=['pasta-pizza','veg-burger'])
keyword_arg(order=['Fruit salad','milk shake'], name="Ananya") #when we provide parameter name, argument order doesn't matter

#default argument
'''
we can't default argument functions like this:

def default_arg(country='India', name):

Remeber, parameter with default value must always be defined after parameters without default value.
'''
def default_arg(name, country='India'): 
    print(f"{name} is from {country}")


default_arg('Ravi')
default_arg('Ananya', 'Nepal') #value for country will be changed from India to Nepal


#variable-length argument 
'''
we want one, no two, no no three or n numbers of arguments than we use virtual-length argument



'''

def virtual_len_arg(*var):
    if len(var)==0:
        return
    for val in var:
        print('item:',val)
    else:
        print("no item left")

virtual_len_arg('Hello','hi','you','me') #four argument
virtual_len_arg(1) 
virtual_len_arg()



#Anonymous Functions
'''
A function without a name so called anonymous function (lambda function).
 -  small one line function
syntax:
    lambda arguments: expression

    we can call these function similary as normal function, let's see
'''

square = lambda x: x**2
print(square(2))
print(square(4))



#return statement
'''
return statement returns an expression, also exits the function.

A return statement with no arguments is the same as return None.
'''

def mul(arg1, arg2):
    product = arg1*arg2
    print (f"Inside the function product of {arg1} * {arg2} is {product}")
    return product


prod_example = mul(2,3)
print(prod_example)





