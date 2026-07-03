#Write a lambda function which accepts one number and returns cube of that number.
cube = lambda no : no * no * no

def main():
    val = int(input("enter a number "))
    ret = cube(val)
    print("The cube is ",ret)


if __name__ =="__main__":
    main()
