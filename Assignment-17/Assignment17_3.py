#3. Write a program which accepts one number from the user and returns its factorial.
def fact(no):
    if no ==0 or no ==1:
        return 1
    return no * fact(no-1)
def main():
    val = int(input("Enter a number"))
    ret = fact(val)
    print("Factorial is ",ret)
if __name__=="__main__":
        main()

