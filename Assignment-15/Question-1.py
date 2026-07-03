#Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
sqr =lambda no : no*no

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = list(map(sqr,data))
    print(res)


if __name__ == "__main__":
    main()
