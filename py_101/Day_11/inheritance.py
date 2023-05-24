# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child classes inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak() method on the instances
print(dog.name + ": " + dog.speak())  # Output: Buddy: Woof!
print(cat.name + ": " + cat.speak())  # Output: Whiskers: Meow!
