#1. Write a program which accepts N numbers from the user and stores them into a list. Return the addition of all elements from that list.
def DigitsX(no):
    sum=0
    for i in no:
        sum += i
    return sum

def main():
    val = int(input("Enter Size of List: "))
    listx=[]
    for i in range(val):
        io= int(input("Enter a number :"))
        listx.append(io)
    ret =DigitsX(listx)
    print(ret)
if __name__=="__main__":
        main()


