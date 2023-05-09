'''
Built-in String Methods covered:

upper()
lower()
capitalize()
len()
count(str,start,end)
startswith(prefix,start,end)
endswith(suffix,start,end)
strip()
rstrip()
lstrip()
index()
find()
rfind()
replace(old, new [,max])
split()
splitlines()
join()

'''

sample_string = "This string is to be used by every method that requires sample. Feel free to call it"
another_sample = '''
It'll be same, as typed
it keeps everything same, space it's tab and everything is same
feel free to use it!
'''

print(another_sample) #prints exactly same 


#upper()
str = 'get out!' # string has no weight
str_upper = str.upper()
print("str with weight:", str_upper)

#lower()
upr_str = 'GIVE ME MONEY!' #scarry!
str_lower = upr_str.lower()
print("upr_str in lower tone:",str_lower)

#capitalize()
#remember school days teacher taught us to write the first letter of each word in Capital case

camel_case = str_lower.capitalize()
print('Camel case:',camel_case)

#len()
str_length = len(sample_string)
print('Sample string length is :',str_length)

#count()
str_count = sample_string.count('is')
print('Total number of "is" in string is',str_count) #it will include substring as well as individual word and give you count 2, This(is) and is 
str_count_index = sample_string.count('ng',5,str_length)
print('total "ng" occurance is:', str_count_index)
str_space_count = sample_string.count(' ')
print('total "blank space" occurance is:', str_space_count)

#startswith()
'''
returns True if given string starts with a specified prefix, and False otherwise.
'''
prefix_ok = sample_string.startswith('Th')
print('prefix is okay:',prefix_ok)
prefix_ok = sample_string.startswith('This is')
print('prefix is okay:',prefix_ok)
prefix_ok = sample_string.startswith('This string')
print('prefix is okay:',prefix_ok)


#endswith()
'''
returns True if given string ends with a specified sufix, and False otherwise.
'''
suffix_ok = sample_string.endswith('it')
print('suffix is okay:',suffix_ok)
suffix_ok = sample_string.endswith('call it')
print('suffix is okay:',suffix_ok)
suffix_ok = sample_string.endswith(' ') #not ending with empty space
print('suffix is okay:',suffix_ok)

#strip()
special_string = '$$$$Hello World!$$$'
striped_string = special_string.strip('$')
print(striped_string) #removes leading and trailing characters
special_string_space = "     space      "
remove_space = special_string_space.strip()
print(remove_space) #removes leading and trailing space 

#lstrip()
left_strip = special_string.lstrip('$')
print("left strip:",left_strip)

#rstrip()
right_strip = special_string.rstrip('$')
print("right strip:",right_strip)

#index()
'''
returns index of first occurrence of character specified
'''
print('index():',sample_string.index('i'))
print('index() --- delimiter " ":',sample_string.index(' '))


#find()
search_string = another_sample.find("tab") #returns the index of first occurrence (or '-1' if not found)
print(search_string)
another_search = special_string.find('or')
print(another_search)

#rfind()
'''
this is similar to find() method just does work from right end of the string. and gives index of "first occurrence" from right end
'''
find_string = "Hello World!" # we have three 'l' let's see what index we get
left_search = find_string.find('l') # returns 2
right_search = find_string.rfind('l') # return 9
not_found = find_string.rfind('k') # k literal is not present so return -1

print('left search:', left_search)
print('reverse search:', right_search)
print('not found: ', not_found)


#replace(string, new string, max replacement )
'''
create new string from old :)
'''
orignal_string = 'pussy cat pussy cat, where have you been? pussy cat pussy cat, have you eaten my bean?'

new_string = orignal_string.replace('pussy','black') #replaces all pussy with black 
print("orignal string:", orignal_string)
print("new string:",new_string) 

two_replace_only = orignal_string.replace('pussy','black',2) #replaces first two occurance
print("two replace only:", two_replace_only) 


#split(delimiter,number)
'''
split() splits a string into a list of substrings based on specified delimiter
let's see
'''
sample_split = sample_string.split()
print('sample string split:',sample_split)
dummy_ip = '192.168.0.1'
number_list = dummy_ip.split('.') # gives you list of number
print('split: ',number_list)
only_two_split = dummy_ip.split('.',2)
print('only two split: ',only_two_split)


#splitlines() 
f'''
splits new line character and returns a list of lines, let's use our sample
another_sample variable for this


has an optional parameter (keepends=True) -> this will keep \n at end in list
'''
list_of_lines = another_sample.splitlines()
print(list_of_lines)
keep_end_newline = another_sample.splitlines(keepends=True)
print(keep_end_newline)


#join()
'''
takes sequence of string as argument and concatenates them into a single string, with specified delimiter between each pair of adjacent strings.
'''
joined_string = ':'.join(sample_string)
print("delimiter used ':'",joined_string) #it is too much for example let's try a list

sample_list = ['sec-c','beach','on','beach']
list_join = '--'.join(sample_list)
print('used list, delimiter "--":',list_join)

easy_join_string = ' '.join("givemespace")
print(easy_join_string)