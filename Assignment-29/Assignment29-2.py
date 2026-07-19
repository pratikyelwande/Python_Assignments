#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
import os
def main():
    try:
        fname= input("Enter file Name:")
        fobj=open(fname,"r")
        data=fobj.read()
        print(data)
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()


