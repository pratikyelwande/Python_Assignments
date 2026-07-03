#Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.
checkodd =lambda no : no % 2 !=0

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = list(filter(checkodd,data))
    print(res)


if __name__ == "__main__":
    main()

