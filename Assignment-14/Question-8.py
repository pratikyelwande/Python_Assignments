#Write a lambda function which accepts two numbers and returns addition.
checkadd = lambda no1,no2 : no1 +no2

def main():
    val1 = int(input("enter first number "))
    val2 = int(input("Enter second number :"))
    ret = checkadd(val1,val2)
    print("The addition is ",ret)


if __name__ =="__main__":
    main()
