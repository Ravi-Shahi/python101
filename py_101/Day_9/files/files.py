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


'''
from helper_module.full_form import mode_fullform

file = open("sample_text.txt") # when mode is not mentioned, its read bydeault
# file = open("sample_text.txt","r") #read mode

file_mode = file.mode #returns file is opened in which mode
print('file is opened in:',mode_fullform(file_mode))

