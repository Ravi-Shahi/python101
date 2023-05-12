'''
dictionary is another built in data structure that stores data in key-value pairs.
it is mutable, ordered iterable and do not allow duplicates.
'''
# create dictionary
my_cv = {
    "name": "Ravi",
    "age": 20,
    "job_role": "Automation Developer",
    "age": 23 #overwrites the old one no duplicates allowed
}

print("This is dictionary object:", my_cv)

# access value using key
candidate_name = my_cv['name']
print(f'name of candidate: {candidate_name}')


#loop
for item in my_cv:
    print(item) # gives you keys
print('-----------------------------')
for item in my_cv.items():
    print(item) #tuple (key:value)
print('-----------------------------')
for key in my_cv.keys():
    print(key)
print('-----------------------------')
for value in my_cv.values():
    print(value)