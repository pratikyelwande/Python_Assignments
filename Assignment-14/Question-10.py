#Write a lambda function which accepts three numbers and returns largest number.

checklar = lambda no1,no2,no3 : no1 if no1 > no2 &  no1 >no3 else no2 if no2 > no3 else no3

def main():
    val1 = int(input("enter first number "))
    val2 = int(input("Enter second number :"))
    val3 = int(input("Enter Third number :"))
    
    ret = checklar(val1,val2,val3)

    print("The Largest no is ",ret)


if __name__ =="__main__":
    main()

