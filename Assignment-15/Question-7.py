#Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.
greater =lambda no1 : no1 > 5

def main():
    n= int(input("How many Numbers:"))
    data=[]

    for i in range(n):
        val= int(input("Enter a number"))
        data.append(val)
    res = list(filter(greater,data))
    print(res)


if __name__ == "__main__":
    main()

