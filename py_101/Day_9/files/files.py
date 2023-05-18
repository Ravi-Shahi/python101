'''
This covers basics of file handling in python,
basics operations we can do are:
    1. Create Files
    2. Read Files
    3. Update Files
    4. Delete Files
Performing operations on files follows this order
    a. open file
    b. perform operations
    c. close file


'''
# Open a file
'''
we use open() function to open a file, it takes two parameter filename and mode
There are four different modes for opening a file:
    1. "r" - Read (Default), will give error if file doesn't exists
    2. "w" - write, will create files if file doesn't exists and rewrite the previous contents of the existing file
    3. "a" - append, will create a file is file doesn't exitst and doesn't rewrites the contents of file
    4. "x" - Create, creates file but returns error if file exists

syntax:
    {variable} = open({path/file},{modes})

    we can also choose type of file,
    -   't' - text file
    -   'b' - binary file (images and all..)


once file is opened, we can use methods:
    1. read(size) -- read file content, takes optional argument(number of bytes to read)...if not passed will read entire file
    2. write(str) -- takes string input
    3. close() 


note: 
    It is good practice to use the with keyword when dealing with file objects.
'''
from helper_module.full_form import mode_fullform
from helper_module.check_file_exist import check_file

#create file
new_file = input('Lets check and create your file\n\n Enter filename with extension: ')
if(check_file(new_file)):
    print('file already exist!')
else:
    new_file = open(new_file,'x')
    print('file created!')    
    new_file.close()

file = open(new_file) # when mode is not mentioned, its read by default
# file = open("sample_text.txt","r") #read mode

file_mode = file.mode #returns file is opened in which mode
print('file is opened in:',mode_fullform(file_mode))



#read files | read(no_ofcharacter) method
dumy_file = open('./dummy_file.txt','r') #open() returns file object
# print(dumy_file.read()) #use read() method the text content of file

print('\n just 10 characters:',dumy_file.read(10)) # returns 10 character from file

print('\n read entire content:', dumy_file.read()) # returns remaining  content of file excluding those 10 character, 
'''
so there is something called as "file pointer"...once you read 10 character, file pointer for file object moves 10 bytes and 
when again you call read() method, it returns content after those 10 character where currently file pointer is

===========================================================
    - tell() : will tell your current file position
    - seek(offset, whence) :  will change the current file position
        offset: number of bytes to move the file pointer
        whence:
            0: relative to begining of the file
            1: relative to current position of the file pointer
            2: end of the file
'''
print('\n calling read() again:', dumy_file.read()) # displays no value, because file pointer is at end
dumy_file.seek(0) #resets the position
print('------ After reset:', dumy_file.read())

#lets read lines from file object
'''
single line
    - readline()
all lines
    - readlines()
'''
dumy_file.seek(0)

read_single_line = dumy_file.readline()
print('First Line:', read_single_line)

print('File position:', dumy_file.tell())
read_rest_lines = dumy_file.readlines()
print('\nremaning lines:', read_rest_lines) #returns a list of lines


#close file --> we do it and is best practice to free up resources 
dumy_file.close()

'''
let's follow good practice and use 'with' keyword when we are dealing with file object.
'''

with open('dummy_file.txt','r+') as open_file:
    # set file pointer to end of the file
    open_file.seek(0,2)
    string = "+++++++++++++++++++++++++++++++++++"
    #write the string value to the file
    open_file.write(string)
    #change file pointer to begining
    open_file.seek(0)
    #read file pointer
    print(open_file.read())
    #check wheter file is closed
    print('inside "with" body:',open_file.closed)  

print('outside "with" body:',open_file.closed)   

'''
write method replaces the content of file, let's see
'''

with open('dummy_file.txt','r+') as f:
    f.write('****') #what ever your current content might be, the first four character will be replaced with ****
    print('\n\n',f.read())
    print('current position:',f.tell())