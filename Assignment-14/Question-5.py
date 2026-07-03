#Write a lambda function which accepts one number and returns True if number is even otherwise False.
checkeven = lambda no : no %2==0

def main():
    val = int(input("enter a number "))
    ret = checkeven(val)
    print(ret)


if __name__ =="__main__":
    main()

