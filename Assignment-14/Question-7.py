#Write a lambda function which accepts one number and returns True if divisible by 5.
checkdiv = lambda no : no %5==0

def main():
    val = int(input("enter a number "))
    ret = checkdiv(val)
    print(ret)


if __name__ =="__main__":
    main()

