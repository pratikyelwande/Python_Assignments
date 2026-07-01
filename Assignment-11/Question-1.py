def Prime(no):
    if(no <= 1):
        print("It is not Prime")
    else:
        isprime = True
        for i in range(2,no):
            if( no % i)==0:
                isprime = False
                break
        if isprime == False:
            print(no," is not Prime")

        else:
            print(no,"is prime")

def main():
    print("Enter a Number")
    no=int(input())
    Prime(no)
    #print(ans)

if __name__ == "__main__":
    main()
