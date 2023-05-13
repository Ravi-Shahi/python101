'''
Suppose, we are working on xyz project and our main file is getting lengthy, so what we do is...
we create a file consisting of function definations, variables and classes related to a particular task...so this reusable file is called module
'''

'''
four different ways to import modules 
- import module by module name with correct path
- import function individually 
- import everything
- import module with alias name
'''
# import hello_world  #one way to import module
# from hello_world import greet, hello #import particular function name
# from hello_world import * # import everything from that module
import hello_world as hw

hw.greet()

hw.hello('ravi')