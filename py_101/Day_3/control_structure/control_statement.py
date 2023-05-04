'''
Defination: Loop statement allows us to execute a statement or group of statements
multiple times.

suppose we have to print something multiple time, or we have to perform 10 lines of code more than one time
then, we use LOOPs
    - while loop 
    - for loop
    - nested loops
'''

#while-loop
'''

A while loop will keep executing as long as a given condition is true

syntax:
while expression:
    statement(s)

'''
oreo_count = 10
eating_count = 1
while oreo_count != 0:
    oreo_count -= 1 #comment this line if your father owns oreo, beacause you'll be having infinite oreos, give it a try!
    print(f"I ate' {eating_count} oreo, remaning is {oreo_count}")
    eating_count += 1
else:
    print("Oreo is empty :(")


#For loop 

'''

A for loop will iterate over the items of any sequence, such as string or a list

syntax:
for iterating_variable in sequence:
    statement(s)

elements in sequence will be assigned to iterating_variable and then statement(s) block is executed,
until the entire elements in sequence is exhausted.

'''

for letter in 'ANANYA':
    print(letter)

grocerry_list = ['Rice','Mushroom','Milk','Coffee','kit-kat']

for item in grocerry_list:
    print(item)


'''
we also have a cool function, 

range(start, stop, step), so let's talk about it..

range will  return sequence of number, starting from 0 by default and stops before a specified number (i.e. stop parameter)
step is increment default is 1

start: optional
stop: required
step: Optional

'''

#for loop using range function

for index in range(len(grocerry_list)):
    print(f'Item {index + 1} in list is: {grocerry_list[index]}')

#so len() function gives you total number of elements in list or total number of character in string, we'll learn more 

# Loop control Statements
'''
loop control statement is something which changes the normal execution sequence
Python supports :
    - break: this terminates the loop and transfer the execution to the statement immediately following the loop
    - continue: It skips the remainder of it's body and moves to loop conditions for reiterating
    - pass: It does nothing, we use pass when we have not written code for certain condition...just required for no syntax error situation.

'''

for count in range(1,10):
    if count == 4:
        continue
    if count == 5:
        pass
        print(count,'Using pass')
    print(count)
    
else:
    print("completed!")







'''
we can use else with for loop in python

suppose Ravi and Ananya went to a cafe, and they try to order food...

'''

cafe_menu = ['burger', 'pasta', 'pizza', 'ice-coffee', 'mocha', 'ramen']
ananya_order = ['ice-coffee','pizza', 'choco-lava']
# ananya_order =[]
count = 0
# print(locals())

for item in cafe_menu:
    if len(ananya_order)==0:
        pass
    elif item in ananya_order:
        print("Order Noted!")
        count +=1
    else:
        print("Request Item is not with us!")
else:
    if count !=0:
        print("Thank you for your order. Please wait a few moments while we get everything ready for you")
        count = 0
    else:
        print("Are you ready to Order?")
