#7. Write a program which accepts one number and displays the following pattern.
def Pattern(no):
    for i in range(no):
        for j in range(1,no+1):
            print(j, end=" ")
        print()

def main():
    val = int(input("Enter a number"))
    Pattern(val)
if __name__=="__main__":
        main()


