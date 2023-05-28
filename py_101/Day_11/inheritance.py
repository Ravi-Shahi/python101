'''
when a class inherits the attributes and methods of another class, the process is called Inheritance.
The class which inherits the properties of another class is called "Child class" or "derived class" or "sub class"

The class from which it iinherits is called "Parent class" or "Base class" or "super class"

syntax:

class BaseClass:
    #attributes
    #methods()
    ....

class ChildClass(BaseClass):
    #derived class attributes
    # methods
'''

#base class
class login:
    def __init__(self,user,password):
        self.user = user
        self.password = password
    
    def authenticate(self, user, password):
        if self.user == user and self.password == password:
            print('Authenticated!')
        else:
            print('Unknown User!')

#derived class
class client(login):
    def login(self):
        client_user = input('Enter your username\n')
        client_pass = input('Enter you password \n')
        super().authenticate(client_user, client_pass) # super() is used to call methods of base class

ravi = client("ravindar","123")

ravi.login()

ravi.authenticate('ravindar','123') # Inheritance helps you write DRY code!

