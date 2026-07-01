def Reverse(no):
    rev = 0
    while( no > 0):
        digit  = no % 10
        rev = rev * 10 + digit
        no = no // 10

    return rev


def main():
    val = int(input("Enter a number"))
    Ret = Reverse(val)
    print("Reverse no is : ",Ret)

if __name__ == "__main__":
    main()
