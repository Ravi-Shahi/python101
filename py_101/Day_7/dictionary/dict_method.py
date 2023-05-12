'''
keys()
values()
items()
update()
pop()
popitem()
clear()
copy()
get()
fromkeys()

'''
my_cv = {
    "name":"Ravindar",
    "company": "WIPRO",
    "age": 23,
    "DOJ": 2021
}
# keys()
my_cv_keys = my_cv.keys()
print('keys:',my_cv_keys) #list of keys

# values()
my_cv_values = my_cv.values()
print('values:',my_cv_values) #returns list of values

# items()
my_cv_items = my_cv.items()
print('Key-value pair:',my_cv_items) #returns tuple of list value pair

# update()
my_cv.update({'role':'Automation Developer'}) #inserts an item to dictionary
print('dictionary after update():',my_cv)

# pop()
my_cv.pop('DOJ') #removes an element from dictionary
print('dictionary after pop():',my_cv)

# popitem()
last_inserted = my_cv.popitem()
print('last inserted item was:',last_inserted)

# copy()
cv_copy = my_cv.copy()
print('copy of my cv:',cv_copy)

# clear()
my_cv.clear()
print('removed all item:',my_cv)
my_cv.update(cv_copy)
print('Updated my_cv from cv_copy:',cv_copy)

# get()
name_in_cv = my_cv.get('name')
print('if key-value exist, returns:', name_in_cv)

value_not_present = my_cv.get('role','Automation Developer')
print('if item dosen\'t exist:', value_not_present)

my_cv.update({'role':'Automation Developer'})
check_if_present = my_cv.get('role','Not INtrested!')
print('What will it give? defualt value or:',check_if_present) #returns the actual value present in dictionary


#fromkeys()
list_key = ['from_address','seller','to_address','buyer']
create_dictionary = dict.fromkeys(list_key) #creates new dictionary with list value as keys and None as key's value
print('created dictionary:', create_dictionary)

create_another_dict = dict.fromkeys(list_key,0) #keys will get value 0
print(create_another_dict)

#create dictionary using list
listA = ['one','two','three']
listB = [1,2,3]
dictionary = dict(zip(listA,listB))
print(dictionary)