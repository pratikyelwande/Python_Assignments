def OddNo(value):
    for i in range(1,value+1):
        if(i % 2 !=0):
            print(i)
            

def main():
    print("enter a Number")
    n=int(input())
    OddNo(n)
if __name__ =="__main__":
    main()

