'''
variable is a container with value stored in it.
suppose we want to print something like
    ' Hi, My name is Ravi and my friends name is Ananya. I live with Ananya since 1880.
      Ananya and I are basically ghost of two love birds named Ravi and Ananya.'
to print such type of msg we can use variables as Ravi and Ananya are repeated more than once
we will create variable:
    - {boy} to store value Ravi 
    - {girl} to store value Ananya
'''

boy = 'Ravi'
girl = 'Ananya'

print(f"'Hi, My name is {boy} and my friends name is {girl}. I live with {girl} since 1880. {girl} and I are basically ghost of two love birds named {boy} and {girl}.'")

'''
Suppose Ananya finds someone New or vice-versa than we can change the message just by changing the value of 
variable boy and girl :)
'''
#Another couple
girl = 'Sneha'
boy = 'Raveen'
year = 1800
print(f"'Hi, My name is {boy} and my friends name is {girl}. I live with {girl} since {year}. {girl} and I are basically ghost of two love birds named {boy} and {girl}.'")


'''
best practices to name a variable is
    - use small letters
    - a word or more words seperrated  by underscore to improve readability
'''