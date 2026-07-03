#Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.
from functools import reduce
sumeven =lambda no1 : no1 % 2==0 

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    ret = list(filter(sumeven,data))
    print("Count of Even number is :",len(ret))


if __name__ == "__main__":
    main()


