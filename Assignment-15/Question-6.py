#Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.
from functools import reduce
minix =lambda no1,no2 : no1 if no1 <no2 else no2

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = reduce(minix,data)
    print(res)


if __name__ == "__main__":
    main()


