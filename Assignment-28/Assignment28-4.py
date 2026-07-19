'''Write a program which accepts two file names from the user.

First file is an existing file
Second file is a new file

Copy all contents from the first file into the second file.'''
import sys
def main():
    try:
        first= sys.argv[1]
        second = sys.argv[2]
        
        fobj= open(first,"r")
        data= fobj.read()
        sec= open(second,"w")
        sec.writelines(data)


        fobj.close()
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()


