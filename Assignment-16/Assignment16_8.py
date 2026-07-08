#8. Write a program which accepts a number from the user and prints that many * (asterisks) on the screen.
def display(no):
    for i in range(no):
        print("*", sep=" ")
def main():
    val = int(input("Enter a number"))
    display(val)
if __name__=="__main__":
        main()

