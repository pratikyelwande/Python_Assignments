#Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
divx=lambda no1 : no1 % 5 & 3 ==0

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = list(filter(divx,data))
    print(res)


if __name__ == "__main__":
    main()

