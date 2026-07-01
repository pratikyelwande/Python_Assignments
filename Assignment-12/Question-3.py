Addition = lambda no1,no2:  no1+no2
substraction = lambda no1,no2:  no1-no2
multiplication = lambda no1,no2: no1*no2
division = lambda no1,no2: no1/no2

def main():
    val1=int(input("Enter First Number:"))
    val2 = int(input("Enter Second Number"))
    
    add = Addition(val1,val2)
    print("Addition is : ",add)
    sub = substraction(val1,val2)
    print("ubstraction is : ",sub)
    mult = multiplication(val1,val2)
    print("multiplication is : ",mult)
    div = division(val1,val2)
    print("division is : ",div)

if __name__ == "__main__":
    main()
