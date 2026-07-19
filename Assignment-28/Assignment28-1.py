#Write a program which accepts a file name from the user and counts how many lines are present in the file.

def main():
    try:
        filenm= input("Enter File Name :")
        with open(filenm,"r") as fobj:
            lines =fobj.readlines()
            print(len(lines))
        fobj.close()
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()
