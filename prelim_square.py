import math
class Square:

    def __init__(self, length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def areaSquare(self):
      Area = self.length * self.width * self.height
      return Area

    def perimeterSquare(self):
      Perimeter = 2 * (self.length + self.width)
      return Perimeter

    def printArea(self):
      myArea= self.areaSquare()
      myPerimeter = self.perimeterSquare()
      print ("The area of square" + " is " + str(myArea) + " and the perimeter is " + str(myPerimeter))

square1 = Square(8,9,9)
square1.printArea()
