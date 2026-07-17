class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
        self.Radius = float(input("Enter Radius : "))
    
    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)
   
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius : ",self.Radius)
        print("Area", self.Area)
        print("Circumference :",self.Circumference)


def main():
    obj1=Circle()
    obj2 = Circle()
    print("obj-1 ")
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print("obj-2 ")
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()


if __name__ == "__main__":
    main()

