'''Design a Python application that creates two threads named Prime and NonPrime.

Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.'''
import threading
def Prime(no):
    isPrime=False

    for i in no:
        if i >1:
            isPrime=True
            for j in range(2,i):
                if i % j ==0:
                    isPrime= False
                    break
            if isPrime:
                print(i)

def NonPrime(no):
    NotPrime= False
    for i in no:
        if i <=1:
            print(i)
            continue
        NotPrime=True
        for j in range(2,i):
            if i % j ==0:
                NotPrime=False
                break
        if NotPrime == False:
            print(i)


def main():
    val= int(input("Enter Size of list: "))
    lst=[]
    for i in range(val):
        lst.append(int(input()))

    print("Prime numbers are :")
    t1 = threading.Thread(target=Prime,args=(lst,))
    t1.start()
    t1.join()

    print("Non Prime numbers are : ")

    t2 = threading.Thread(target = NonPrime,args=(lst,))
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()
