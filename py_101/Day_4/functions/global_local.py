'''
Scope is a boundry defined for a variable or function where it can be used in a program.

let's see
'''
#global variable can be accessed gloablly in program
street_dog = "Shibu!"

def doctor():
    # local variable: only accessible to doctor function
    doctor_dog = "Husky!"
    # doctor function can access street_dog variable
    print(f"I'm doctor and I can pet {doctor_dog} as well as {street_dog}")


doctor()

print(f"I'm a stranger I can pet {street_dog}")

#try street_dog instead of doctor_dog \_/
print(f"I'm another stranger I can't pet {doctor_dog}, it'll give an error! may also bite me :(")