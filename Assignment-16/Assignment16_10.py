#10. Write a program which accepts a name from the user and displays the length of that name.
def check(no):
    return len(no)
def main():
    val = input("Enter a name : ")
    ret = check(val)
    print(ret)
if __name__=="__main__":
        main()

