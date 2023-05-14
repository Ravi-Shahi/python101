'''
list comprehension is compact ninja technique to filter out elements from list, tuples or any iterable.

syntax:

[expresion for item in iterable if condition]
'''


#create list of elements that is divisible by 2 in range of 20
# not compact way :(
div_by_two =[]
for num in range(20):
    if num%2==0:
        div_by_two.append(num)

print('Num divisible by 2 are:',div_by_two)


# ninja technique [list comprehension]

divby2 = [num for num in range(20) if num%2==0]
print('compact way:',divby2)


class_1A= ['Abhishek','Akhil','Bucky','Rogers','Ravi','Rocky','Ratish']
name_with_ra = [name for name in class_1A if name.startswith('Ra') or name.startswith('A')]

print('Names Start with "RA"', name_with_ra)