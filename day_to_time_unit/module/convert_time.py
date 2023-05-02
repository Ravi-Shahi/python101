#convert_days_to_unit
def days_to_unit(days,unit):
    if unit == "minutes":
        return f"{days} days equals to {days*24*60} minutes."
    elif unit == "hours":
        return f"{days} days equals to {days*24} hours."
    else:
        return "unsupported unit!!!"

def validate_and_execute(days_and_unit):
    try:
        number_of_days = int(days_and_unit["days"])
        unit = days_and_unit["unit"]
        print(days_to_unit(number_of_days,unit))
    except:
        print("Don't ruin my code! Please enter Integer number of days ")

input_msg = "Hey! Enter number of days and unit to convert: \n'e.g. 24:minutes' or '1:hours'\n"

