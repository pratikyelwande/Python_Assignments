#9. Write a program which accepts a number from the user and returns the number of digits in that number.
def DigitsX(no):
    return len(str(no))

def main():
    val = int(input("Enter a number"))
    ret =DigitsX(val)
    print(ret)
if __name__=="__main__":
        main()



