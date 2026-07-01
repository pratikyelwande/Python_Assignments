def Binarye(no):
    binary=""
    for i in range(no,0,-1):
        binary= str(no%2)+ binary
        no=no//2
        if no==0:

            break

    return binary
def main():
    val = int(input("Enter a number :"))
    Ret = Binarye(val)
    print(Ret)

if __name__ == "__main__":
    main()
