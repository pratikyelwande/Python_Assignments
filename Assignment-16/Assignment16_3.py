#3. Write a program which contains one function named as Add() which accepts two numbers from user and returns addition of that two numbers.
def Add(no1,no2):
    return no1+no2
def main():
    val1=int(input("Enter first number: "))
    val2=int(input("Enter second number:"))
    ret =Add(val1,val2)
    print(f"Addition is {ret}")

if __name__=="__main__":
    main()


