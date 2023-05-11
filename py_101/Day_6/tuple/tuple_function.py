'''
len()
max()
min()
tuple()
'''

sample_tuple = (1,2,30,4,5)

# len()
print(len(sample_tuple)) #output: 5
# max()
print(max(sample_tuple)) #output: 30
# min()
print(min(sample_tuple)) #output: 1
# tuple(seq)
string = "hello"
list = [1,2,3,4,5,6]

str_tuple = tuple(string)
print('string to tuple:',str_tuple)

list_tuple = tuple(list)
print('list to tuple:',list_tuple)
