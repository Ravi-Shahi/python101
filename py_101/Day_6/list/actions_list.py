'''
functions
    - len()
    - max()
    - min()
    - list()
Iteration
membership
repetion
Concatenation
'''

list_sample = [1,2,3,4,5]

# len()--> size of list
list_size = len(list_sample)
print('Total size of list:',list_size)

# max()
print('Max value:', max(list_sample))

# min()
print('Min value:',min(list_sample))

# list() #conversion iteratable objects to list
tupple = (1,2,3,4,5,6,7,8)
print('tuple:',tupple)
tupple_list = list(tupple)
print('converted to list',tupple_list)
string = "Ravi has crush on Ananya, She is a Singer!"
print('string',string)
string_list = list(string)
print('converted to list:',string_list)



# print list elements
for item in list_sample:
    print(item)
else:
    print("That's it!")

for index in range(len(list_sample)):
    print(f'Index {index}: {list_sample[index]}')
else:
    print('completed!')

#membership
mem_list = ['one','%%','||','two',12,34]

found = 'is' in mem_list
print('Found:',found)
found = 'one' in mem_list
print('Found:',found)


#repetition
repeat_list = ['hello','boy!']
print('Orignal List:', repeat_list)
repeat_two_times = repeat_list*3
print('Repeat Two Times',repeat_two_times)

#concatenation
list1 = ['one','two','three','four']
print('List one:', list1)

list2 = ['five','six','seven','eight']
print('List two:', list2)

list3 = list1 + list2
print('Concatenated list:',list3)

