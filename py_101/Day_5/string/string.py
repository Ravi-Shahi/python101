'''
Enclose characters in quotes, string is created.
let's see
'''

#variable of string type, enclosed character is string literal
string_one = "I'm String!"
string_two = "123"
string_three = " "
string_four = ";}]]]]///\\\\" # '\' is used to escape some special character, '\' is known as escape sequence

# as writen Enclosed characters in quotes are string :)
print(string_one,':',type(string_one))
print(string_two,':',type(string_two))
print(string_three,':',type(string_three))
print(string_four,':',type(string_four))

# Accessing string
'''
suppose "Ananya" is string
we can access each element of anaya using square bracket [] 

lets see

index 012345
str = Ananya

str[0] gives 'A'
str[1] gives 'n'
str[2] gives 'a'

we can also access last character
str[-1] gives 'a'
str[-2] gives 'y'
'''

#slice
my_girl = 'Ananya' # double quotes or single ...python is okay with both 
print(my_girl[0])
print(my_girl[2])
print(my_girl[-1])
print(my_girl[-2])

#Range
my_girl_likes = 'Ananya_likes_to_eat_Dosa_and_ice-cream_together' # '_' in place of blank space to make point clear

print(my_girl_likes[0:6]) # extracts first five words
print(my_girl_likes[:6]) # does same if we don't mention starting index (by default takes 0th index)

print(my_girl_likes[6:10]) # extract word of index 6-9 i.e. _lik


#Membership operator
another_string = "xyz and zyx in some some thing you got"
gives_bool_val = 'xyz' in another_string
this_will_also = 'ananya' in another_string
neg_this_will_also = 'ananya' not in another_string  
print('gives_bool_val',gives_bool_val) # gives true
print('this_will_also:',this_will_also) # gives false 
print('neg_this_will_also: ',neg_this_will_also) # gives true when not found
print('yz' in another_string) # gives true








