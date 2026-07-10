#Write a program which contains filter(), map() and reduce() in it. The Python application contains one list of numbers. The list contains the numbers accepted from the user
#Filter all even numbers.
#Use map() to calculate the square of each number.
#Use reduce() to return the addition (sum) of all the numbers.

from functools import *

Checkeven =  lambda no :(no % 2==0)

sqr = lambda no : no*no

add= lambda x,y : x + y
def main():
    val=int(input("Enter a List Size : "))
    listx=[]
    for i in range(val):
        lx= int(input("Enter a number: "))
        listx.append(lx)
    print("Youre List : ",listx)
    
    fdata=list(filter(Checkeven,listx))
    print("Data after Filter : ",fdata)

    mdata= list(map(sqr,fdata))
    print("Data after Map :", mdata)

    rdata = reduce(add,mdata)
    print("Data after Reduce : ",rdata)

    
if __name__ == "__main__":
    main()


