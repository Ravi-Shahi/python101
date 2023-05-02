'''
software is useless, if it is not interactive and does it's own
So to make it interactive, we are going to take input from users
    - to change US dollar to Indian Rupay
'''
# display what information we need from user and store it in a variable
amount_us = input("Enter your amount in Dollar \n")

#current value of us dollar
ONE_DOLLAR_VAL = 81.72

#convert dollar to Rupay
amount_india = ONE_DOLLAR_VAL * float(amount_us)

#display the converted data
print(f"{amount_us} dollar is {amount_india} Rupay.")




