from module.convert_time import *

user_input = "" 
while user_input != "exit":
    try:
        user_input = input(input_msg)
        user_input_list = user_input.split(':')
        days_and_unit = {
            "days":user_input_list[0],
            "unit":user_input_list[1]
            }
        validate_and_execute(days_and_unit)
    except:
        print("Press 'exit' to quit!")



