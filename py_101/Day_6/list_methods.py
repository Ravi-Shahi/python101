'''
append()
extend()
count()
index()
insert()
pop()
remove()
reverse()
sort()
'''

#append(obj)
'''
appends a passed passed obj into the existing list.
'''
list = ['one','two','three','four']
print('existing list:',list)
list.append('five')
print('after apending, list:', list)

another_list = ['six','seven','eight','nine']
list.append(another_list) # problem here is another_list will be appended as one element in list, index will be 5 not as seperate elements
print('After appending list:',list) # Output: ['one','two','three','four','five',['six','seven','eight','nine']]

#extend(seq)
'''
it solves the problem of appending one list to another
'''
list_one = [1,2,3,4,5]
list_two = [6,7,8,9,10]
list_one.extend(list_two)
print('List one after extend method', list_one)

#count(obj)
'''
count returns number of times object in list occurs. let's see
'''
student_1A = ['Ravi','Shashi','Akash','Vikash','Ravi','Sashi','Mandeep','Ayush','Akash']
total_ravi_1A = student_1A.count('Ravi')
print("number of student name Ravi in class:",total_ravi_1A)
total_shashi_1A = student_1A.count('Shashi')
print("number of student name Shashi in class:", total_shashi_1A)

# index()
'''
returns index of passed object
'''
ravi_index = student_1A.index('Ravi') #returns the lowest index
print('Ravi\'s index:',ravi_index) # Output: 0

'''
gives valueError cause Ananya is not is the list
# ananya_index = student_1A.index('Ananya')
# print(ananya_index)
'''

# insert(index, obj)
'''
used to adjust the list and insert object into list
'''
list = [1,2,3,5]
print('Before insert: ', list)
list.insert(3,4)
print('After insert:', list)

# pop(index) --> parameter is optional
removed_item = list.pop() #removes the last object from list
print('used pop: ', list)
print('removed element', removed_item)
another_removed_item = list.pop(2)
print('used pop with argument 2:',list)
print('removed element', another_removed_item)

# remove()
'''
looks for matching object and removes it from list
'''
mixed_list = ['hello',1,'world',1234,'Marry']
print('Orignal list:', mixed_list)
mixed_list.remove(1234)
print('list after removing 1234:', mixed_list)


# reverse()
'''
as name suggest reverse a list
'''
org_list = [1,2,3,4,5]
print('Orignal list:', org_list)
org_list.reverse()
print('Reversed List', org_list)


# sort()
something_messy = [69,89,12,0,23,444,566,999]
print('messed up list:',something_messy)
something_messy.sort()
print("sorted list:",something_messy)