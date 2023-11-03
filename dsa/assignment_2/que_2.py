class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    #setter
    def setRadius(self, radius):
        self.radius = radius
    
    #getter
    def getRadius(self):
        return self.radius

    def getArea(self):
        return 3.14 * (self.radius*self.radius)

    def getCircumference(self):
        return 2*3.14*self.radius


try:
    c1 = Circle(5)
    print(c1.getRadius())
    c1.setRadius(4)
    print(c1.getArea())
    print(c1.getCircumference())
except Exception as e:
    print(f"Error is {e}")