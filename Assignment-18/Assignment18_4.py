#4. Write a program which accepts N numbers from the user and stores them into a list. Accept one another number from the user and return the frequency of that number from the list.

def DigitX(no,src):
    temp=no[0]
    cnt=0
    for i in no:
        if( src== i ):
            cnt+=1

    if cnt == 0:
        print("Search number is not in the List.")
    return cnt  


def main():
    val = int(input("Enter Size of List: "))
    listx=[]
    for i in range(val):
        io= int(input("Enter a number :"))
        listx.append(io)
    src= int(input("Enter Number to search: "))

    ret =DigitX(listx,src)
    print(ret)
if __name__=="__main__":
        main()


