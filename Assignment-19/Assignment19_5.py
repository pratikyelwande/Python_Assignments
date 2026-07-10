#Write a program which contains filter(), map() and reduce() in it. The Python application contains one list of numbers accepted from the user.
#Filter all prime numbers.
#Use map() to multiply each number by 2.
#Use reduce() to return the maximum number from the resulting list.

from functools import *

def checkPrime(no):
    if no <=1:
        return False
    for i in range(2,no):
        if no % i ==0:
            return False
    return True

Mul = lambda no : no*2

Max= lambda x,y : x if x > y else y
def main():
    val=int(input("Enter a List Size : "))
    listx=[]
    for i in range(val):
        lx= int(input("Enter a number: "))
        listx.append(lx)
    print("Youre List : ",listx)
    
    fdata=list(filter(checkPrime,listx))
    print("Data after Filter : ",fdata)

    mdata= list(map(Mul,fdata))
    print("Data after Map :", mdata)

    rdata = reduce(Max,mdata)
    print("Data after Reduce : ",rdata)

    
if __name__ == "__main__":
    main()


