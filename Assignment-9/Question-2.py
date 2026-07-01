def ChkGreater(value1,value2):
    if (value1 == value2):
        return value1
    else:
        return value2

def main():
    print("Enter first number:")
    value1=int(input())
    print("Enter Second number")
    value2=int(input())
    ans=ChkGreater(value1,value2)
    print("Greater Number is :")
    print(ans)


if __name__ =="__main__":
    main()

