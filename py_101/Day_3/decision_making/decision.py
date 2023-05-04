'''
Decision making is anticipation of conditions occuring while execution of the program and 
specifying actions taken according to the conditions.

'''

raining = True
pizza_cafe_open = False
indian_cafe_open = True
#simple decision
if raining:
    print("Let's Order Food!")
else:
    print("Let's cook Food!")

#little more decision
if raining and pizza_cafe_open:
    print("Let's order pizza!")
elif raining and indian_cafe_open:
    print("Let's order kadhai paneer!")
else:
    print("Let's cook food!")


#Let's not repeat type decision or nested decisions
if raining:
    print("Let's order Food!")
    if pizza_cafe_open:
        print("Let's order Pizza!")
    elif indian_cafe_open:
        print("Let's order Panner!")
    else:
        print("Cook Food!")
else:
    print("call Ananya for Food!")




    