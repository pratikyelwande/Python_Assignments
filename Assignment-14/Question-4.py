#Write a lambda function which accepts two numbers and returns minimum number.
lowest = lambda no1,no2 : no1 < no2

def main():
    val1 = int(input("enter first number "))
    val2 = int(input("enter second number "))
    ret = lowest(val1,val2)
    if (ret == True):
        print("The Lowest no is ",val1)
    else:
        print("The Lowest no is ",val2)


if __name__ =="__main__":
    main()

