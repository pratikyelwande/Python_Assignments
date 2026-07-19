#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
def main():
    try:
        fname= input("Enter file Name:")
        word= input("Enter a word that you want to search:")
        
        with open(fname,"r") as fobj:
            data=fobj.read()
            datax= data.split()
            flag=False
            for i in datax:
                if word == i:
                    flag=True
            if( flag == True):
                print("Word is Exist")
            else:
                print("Word is not exist")
        fobj.close()
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()



