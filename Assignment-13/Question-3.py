def Perfect(no):
    sum=0
    for i in range(1,no):
        if (no % i ==0):
            sum += i
    return sum
def main():
    val=int(input("Enter a number:"))
    Ret = Perfect(val)
    if (Ret == val):
        print("It is a Perfect No", Ret)
    else:
        print("It is not a Perfect No",Ret)


if __name__ =="__main__":
    main()
