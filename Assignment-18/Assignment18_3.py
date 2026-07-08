#3. Write a program which accepts N numbers from the user and stores them into a list. Return the minimum number from that list.
def DigitX(no):
    min=no[0]
    for i in no:
        if i < min:
            min=i

    return min
        

def main():
    val = int(input("Enter Size of List: "))
    listx=[]
    for i in range(val):
        io= int(input("Enter a number :"))
        listx.append(io)
    ret =DigitX(listx)
    print(ret)
if __name__=="__main__":
        main()


