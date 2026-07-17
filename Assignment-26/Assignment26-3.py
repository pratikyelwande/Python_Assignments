class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))
    
    def Addition(self):
        return self.Value1 + self.Value2
   
    def Substraction(self):
        return self.Value1 - self.Value2   

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2
   
    def Display(self):
        print("Addition : ",self.Addition())
        print("subtraction", self.Substraction())
        print("Multiplication :",self.Multiplication())
        print("Division :",self.Division())


def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    print("Object 1")
    obj1.Accept()
    obj1.Display()

    print("-"*10)

    print("Object 2")
    obj2.Accept()
    obj2.Display()

if __name__ == "__main__":
    main()

