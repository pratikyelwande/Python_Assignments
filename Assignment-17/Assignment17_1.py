#1. Create one module named Arithmetic which contains four functions:Add() for addition,Sub() for subtraction,Mult() for multiplication,Div() for division,All functions should accept two parameters as numbers and perform the respective operation,Write a Python program that accepts two numbers from the user and calls all the functions from the Arithmetic module.

from Arithematic import * 

def main():
    val1 = int(input("Enter First number"))
    val2 = int(input("Enter Second number :"))
    sum = Add(val1,val2)
    print("Addition is ",sum)
    substract= Sub(val1,val2)
    print("Substraction is ", substract)
    multi = Mul(val1,val2)
    print("Multiplication is ", multi)
    Divi= Div(val1,val2)
    print("Division is ", Divi)
if __name__=="__main__":
        main()

