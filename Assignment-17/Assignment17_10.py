#10. Write a program which accepts a number from the user and returns the addition of digits in that number
def DigitsX(no):
    sum=0
    for i in no:
        sum =sum + int(i)
    return sum
    

def main():
    val = input("Enter a number")
    ret =DigitsX(val)
    print(ret)
if __name__=="__main__":
        main()


