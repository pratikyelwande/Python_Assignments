#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
def main():
    try:
        filenm= input("Enter File Name :")
        with open(filenm,"r") as fobj:
            lines =fobj.read()
            print(lines)

        fobj.close()
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()


