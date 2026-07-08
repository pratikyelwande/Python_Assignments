#5. Write a program which accepts N numbers from the user and stores them into a list. Return the addition of all prime numbers from that list.The main Python file accepts N numbers from the user and passes each number to the ChkPrime() function, which is part of the user-defined module named MarvellousNum.The function in the main Python file should be named ListPrime().
from MarvellousNum import *

def ListPrime(no):
    sum=0
    for i in no:
        if ChkPrime(i):
            sum+= i
    return sum
    

        

def main():


    val = int(input("Enter Size of List: "))
    listx=[]
    for i in range(val):
        io= int(input("Enter a number :"))
        listx.append(io)
    ret =ListPrime(listx)
    print(ret)


if __name__=="__main__":
        main()


