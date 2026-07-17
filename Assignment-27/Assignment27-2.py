class BookAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self):
        x=int(input("How much amount you want to Deposit :"))
        self.Amount += x

    def Withdraw(self):
        draw = int(input("How much amount you want to Withdraw :"))
        if draw <= self.Amount:
            self.Amount -= draw
        else:
            print("Insufficent Balance")
        return self.Amount

    def CalculateInterest(self):
        Interest = (self.Amount * BookAccount.ROI)/100
        return Interest


    def Display(self):
        print(f"Holder Name is {self.Name} and Current Balance is {self.Amount}")
        print(f"Interest : {self.CalculateInterest()}")

def main():
    obj1 = BookAccount("Pratik",1000)
    obj2 = BookAccount("Vijay",5000)
    obj1.Withdraw()
    obj1.Display()

if __name__ == "__main__":
    main()


