'''
suppose, I have 10 students of class 1 'A' and I want to use there name in my code
ways to do it is by defining variables:
student_1A_1 = 'Ravi'
student_1A_2 = 'Ananya'
student_1A_3 = 'Sneha'
student_1A_4 = 'Abhishek'
..
.... and so on, but do you think it is efficent way to do the task? no!
so, to handle multiple values we use "LIST"

LIST is nothing but values enclosed in square bracket separated by comma, each item inside list
is given a number called 'index' which starts from zero '0'.
'''

#creating list of students of class 1 'A'
student_1A = ['Ravi','Abhishek','Mohan','Ravindar','Ananya','Sneha','Geeta','Megha','Reet','Preet']

#access list using slice
print('first item of list is:',student_1A [0])
print('second item of list is:',student_1A[1])
print('third item of list is:',student_1A[2])

#access items from other end 
print('last item of list is:',student_1A[-1])
print('second last item of list is:',student_1A[-2])

#access items in range
print('second item to eighth item:',student_1A[1:9]) # [start:end] prints item from start to end-1 


#update items
print("Before change index 1:", student_1A[1])
student_1A[1] = 'Aditi'
print("After update index 1:", student_1A[1])


#update multiple elements from index 2 to 4
print('index 2 to 4:',student_1A[2:5])
student_1A[2:5] = ['Rajeev','Nitish','Bhola','Shyaam']
print('updated list:',student_1A)

