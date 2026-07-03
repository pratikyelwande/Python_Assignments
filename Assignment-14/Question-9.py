#Write a lambda function which accepts two numbers and returns multiplication.

checkmul = lambda no1,no2 : no1 * no2

def main():
    val1 = int(input("enter first number "))
    val2 = int(input("Enter second number :"))
    ret = checkmul(val1,val2)
    print("The multiplication is ",ret)


if __name__ =="__main__":
    main()
