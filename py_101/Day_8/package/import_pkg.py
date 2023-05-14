'''
Package is structuring python's module in directory structure, directory which consists of module, subpackages or sub-suppackages.

IMPORTANT:
    - to treat a directory containing python modules as package __init__.py file is necessary.
'''


# from greet import greet_user,hello_world,world_user
from greet import * #this is bad practice for production
'''
not to import all modules or use asterisk(*) sign we need to add
__all__ = [module1,module2,module3] (names of modules we want to export when package encounters (*)),
inside __init__.py file

note:
    - In production "from package/module import *" is considered as bad practice
    - In fact "from package/module import module/function" is suggested notation
'''
greet_user.greet_user("Ravi!")

to_check_module_contents = dir(multi_fun)
print("module contents:", to_check_module_contents)
multi_fun.fun1()
