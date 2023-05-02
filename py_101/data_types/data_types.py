'''
In our life, we deal with different types of values such as
    - name,
    - count, 
    - amount,
    - proposal_response,
    - grocery_list
    - professionals_cv
Now, to store all this different types of data we have different types of 
data type such as:
    - name: string,
    - count: integer, 
    - amount: float,
    - proposal_response: boolean,
    - grocery_list: list, tupple, set
    - professionals_cv: dictionary
'''

my_name = 'Ravi'
my_age = 69
my_salary = 15.90
ananya_response = False
sneha_response = True

# ordered-list [Ma's list]
monthly_grocerry = ['potato','onion','rice','spices','dal']
# absolute list [Papa's list]
papa_list = ('apple','lemon','watermelon')
# unordered-list [Family's list]
family_list = {'pizza','butter-chicken','ice-cream','pasta'}


my_cv ={
    'name':'Ravindar',
    'age': 69,
    'corrent_company': 'WIPRO',
    'salary': 500,
    'skills': ['python','django']
}

#display
print(f"{my_name} is {my_age} years old, salary is {my_salary}.")
print(f"Ananya is my girlfriend {ananya_response},\nSneha is my girl {sneha_response}")

print(f"Ma gave me list which I can change if I want is: {monthly_grocerry}")
print(f"Papa's list is absolute, can't change is {papa_list}")
print(f"I am servent of house, everyone game me list and that is {family_list}")


print(f"This is my short CV, if you have any suitable job. Please refer to info below \n {my_cv}")

