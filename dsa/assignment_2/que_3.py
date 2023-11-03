class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    #setter
    def setDimensions(self, length,breadth):
        self.length = length
        self.breadth = breadth

    #getter
    def showDimensions(self):
        return (self.length,self.breadth)
    
    def getArea(self):
        return self.length*self.breadth
    
try:
    r1 = Rectangle(2,4)
    print(r1.showDimensions())
    r1.setDimensions(3,9)
    print("After setter:", r1.showDimensions())
    print("Area", r1.getArea())
except Exception as e:
    print(Exception)
