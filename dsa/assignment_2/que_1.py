class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, age: {self.age}")

try:
    ravi = Person("Ravi", 18)
    ravi.show()
    nuannuan = Person("Chin-nuan", 78)
    nuannuan.show()
except:
    print('Fix your code!')

        