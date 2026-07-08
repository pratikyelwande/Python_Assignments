#6. Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

def check(no):
    if no > 0:
        print("Positive")
    elif no == 0:
        print("Zero")
    else:
        print("Negative")
def main():
    val = int(input("Enter a number"))
    check(val)
if __name__=="__main__":
        main()
