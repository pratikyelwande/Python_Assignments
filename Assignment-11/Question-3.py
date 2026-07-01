def Sum(no):
    sum=0
    for i in str(no):
        sum += int(i)
    return sum

def main():
    value = int(input("Enter a number :"))
    Ret = Sum(value)
    print("The Sum of Digit is :",Ret)

if __name__ == "__main__":
    main()
