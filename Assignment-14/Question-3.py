#Write a lambda function which accepts two numbers and returns maximum number.
greatest = lambda no1,no2 : no1 > no2

def main():
    val1 = int(input("enter first number "))
    val2 = int(input("enter second number "))
    ret = greatest(val1,val2)
    if (ret == True):
        print("The Greatest no is ",val1)
    else:
        print("The greatest no is ",val2)


if __name__ =="__main__":
    main()
