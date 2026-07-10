#Write a program which contains one lambda function which accepts one parameter and returns the power of two.

pwr = lambda no : no ** 2

def main():
    val=int(input("Enter a number: "))

    ret = pwr(val)
    print(f" Power of {val} is {ret}")

if __name__ == "__main__":
    main()
