'''Design a Python application that creates two threads named EvenList and OddList.

Both threads should accept a list of integers as input.

The EvenList thread should:

Extract all even elements from the list.
Calculate and display their sum.

The OddList thread should:

Extract all odd elements from the list.
Calculate and display their sum.
Threads should run concurrently.'''

import threading

def EvenList(no):
    sum=0
    for i in no:
        if i % 2 ==0:
            print(i)
            sum += i
            print("Even Sum is : ",sum)
        

def OddList(no):
    sum=0
    for i in no:
        if i % 2 != 0:
            print(i)
            sum += i
            print("Odd sum is : ",sum)

def main():
    slst = int(input("Enter list size :"))
    lst=[]
    for i in range(slst):
        val= int(input("Enter a number : "))
        lst.append(val)

    t1 = threading.Thread(target = EvenList, args=(lst,))
    t2 = threading.Thread(target= OddList, args =(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    main()

