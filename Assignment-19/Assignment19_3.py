#Write a program which contains filter(), map() and reduce() in it. The Python application contains one list of numbers. The list contains the numbers accepted from the user
#Filter all numbers that are greater than or equal to 70 and less than or equal to 90.
#Use map() to increase each number by 10.
#Use reduce() to return the product of all the numbers.
from functools import *

Filterx= lambda no :no >=70 and no <=90

Inc = lambda no : no+10

Product= lambda x,y : x *y
def main():
    val=int(input("Enter a List Size : "))
    listx=[]
    for i in range(val):
        lx= int(input("Enter a number: "))
        listx.append(lx)
    print("Youre List : ",listx)
    
    fdata=list(filter(Filterx,listx))
    print("Data after Filter : ",fdata)

    mdata= list(map(Inc,fdata))
    print("Data after Map :", mdata)

    rdata = reduce(Product,mdata)
    print("Data after Reduce : ",rdata)

    
if __name__ == "__main__":
    main()

