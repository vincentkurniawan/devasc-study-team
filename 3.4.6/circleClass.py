# VINCENT KURNIAWAN - 6181901024

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def circumference (self):
        pi = 22/7
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue
    
    def printCircumference (self):
        myCircumference = self.circumference()
        print ("Circumference of a circle wih a radius of " + str(self.radius) + " is " + str(myCircumference))

circle1 = Circle(2)
circle1.printCircumference()

circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()