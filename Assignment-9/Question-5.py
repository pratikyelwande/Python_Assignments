def Divisible(value):
    if(value % 3==0 and value % 5==0):
        print(value," is divisible by 3 and 5")
    else:
        print("Not Divisible 3 and 5")

def main():
    print("enter a Number")
    n=int(input())
    Divisible(n)
    

if __name__ =="__main__":
    main()
