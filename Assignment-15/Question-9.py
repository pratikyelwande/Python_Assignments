#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce
sumx =lambda no1,no2 : no1*no2 

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = reduce(sumx,data)
    print(res)


if __name__ == "__main__":
    main()

