#Write a program which contains one function named as ChkNum() which accepts one parameter as number. If number is even then it should display "Even Number" otherwise display "Odd Number" on console.
#Example:
#Input: 11 → Output: Odd Number
#Input: 8 → Output: Even Number

def ChkNum(no):
    if(no%2==0):
        print("Even Number")
    else:
        print("Odd number")

def main():
    val=int(input("Enter a number: "))

    ChkNum(val)

if __name__=="__main__":
    main()

