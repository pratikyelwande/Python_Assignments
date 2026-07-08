#2. Write a program which accepts one number and displays the following pattern.
def pattern(no):
    for i in range(no):
        print("*"* no)

def main():
    val = int(input("Enter a number"))
    pattern(val)
if __name__=="__main__":
        main()

