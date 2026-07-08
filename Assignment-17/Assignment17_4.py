#4. Write a program which accepts one number from the user and returns the addition of its factors.
def AddFactor(no):
    sum=0
    for i in range(1,no-1):
        if no % i ==0:
            sum += i
    return sum

def main():
    val = int(input("Enter a number"))
    ret=AddFactor(val)
    print(ret)
if __name__=="__main__":
        main()

