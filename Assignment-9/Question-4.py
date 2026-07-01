def Cube(value):
    print("Cube Root is")
    return value *value *value

def main():
    print("enter a Number")
    n=int(input())
    ans=Cube(n)
    print(ans)

if __name__ =="__main__":
    main()
