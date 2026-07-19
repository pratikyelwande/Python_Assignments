#Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
import os
def main():
    try:
        fname= input("Enter file Name:")
        if os.path.exists(fname):
            print("File Exists")
        else:
            print("File does not Exists")
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()

