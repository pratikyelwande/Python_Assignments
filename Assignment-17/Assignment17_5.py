#5. Write a program which accepts one number from the user and checks whether the number is prime or not.

def Checkprime(no):
    if no <= 1:
        return False
    for i in range(2,no):
        if no % i ==0:
            return False
    return True


def main():
    val = int(input("Enter a number"))
    ret=Checkprime(val)
    if ret == True:
        print("Its a Prime number")
    else:
        print("Not a prime number")
if __name__=="__main__":
        main()

