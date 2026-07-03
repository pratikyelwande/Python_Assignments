#Write a lambda function which accepts one number and returns square of that number.
srq = lambda no : no * no

def main():
    val = int(input("Enter a number: "))
    ret = srq(val)
    print(f"Square root of {val} is ",ret)

if __name__ == "__main__":
    main()
