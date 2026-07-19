#Write a program which accepts a file name from the user and counts the total number of words in that file.
def main():
    try:
        filenm= input("Enter File Name :")
        with open(filenm,"r") as fobj:
            lines =fobj.read()
            count=0
            words = lines.split()
            for i in words:
                count +=1
            print("No of words are :",count)

        fobj.close()
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()

