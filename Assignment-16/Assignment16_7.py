#7. Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5, otherwise returns False.
def check(no):
    if no % 5 ==0:
        return True
    else:
        return False
def main():
    val = int(input("Enter a number"))
    ret = check(val)
    print(ret)
if __name__=="__main__":
        main()

