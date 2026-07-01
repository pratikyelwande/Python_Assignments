def Factorial(value):
    if value==0:
        return 1
    return value * Factorial(value-1)

def main():
    print("enter a Number")
    n=int(input())
    ans=Factorial(n)
    print(ans)

if __name__ =="__main__":
    main()
