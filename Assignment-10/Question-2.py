def Sum(value):
    ans=0
    for i in range(1,value+1):
        ans += i
    print(ans)
def main():
    print("enter a Number")
    n=int(input())
    Sum(n)

if __name__ =="__main__":
    main()
