'''
same as list just, it can't be modified (immutable)
if we replace [] with () it becomes tuple

list = [1,2,3,4,5]
tuple = (1,2,3,4,5)

note: 
string = "one"
tuple = ("one"), both are same unless you put a comma tuple = ("one",)

'''

str = "one"
tuple = ("one")

print(type(str))
print(type(tuple)) #() is used for grouping or separating literals so add ',' to make this tuple
tuple = ("one",)
print(type(tuple))


# access tuple

sample_tuple = ('one','two','three','four')
print("Access fourth element: ",sample_tuple[3])

print("Access range 2-3:",sample_tuple[1:4])

#updating tuple
# sample_tuple[0] = 1 #not allowed, already mentioned its immutable
'''
we can add two tuple though
'''
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print('tup1 + tup2 =',tup3)

#delete tuple
del tup1
# print('tup1 is deleted:',tup1)