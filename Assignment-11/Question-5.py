def Palindrome(no):
    flag = False
    rev=0
    while no > 0:
        digit = no %10
        rev = rev * 10 +digit
        no = no //10
    return rev

def main():
    val =int(input("Enter a number"))
    Ret = Palindrome(val)
    if (Ret == val):
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")

if __name__ == "__main__":
    main()
