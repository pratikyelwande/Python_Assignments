'''Design a Python application that creates two threads.

Thread 1 should calculate and display the maximum element from a list.
Thread 2 should calculate and display the minimum element from the same list.
The list should be accepted from the user.'''

import threading
def Max(data):
    max=data[0]
    for i in data:
        if i> max:
            max=i
    print("Max No is ",max)

def Min(data):
    min=data[0]
    for i in data:
        if i < min:
            min=i
    print("Min no is ",min)


def main():
    val= int(input("Enter Size of list: "))
    lst=[]
    for i in range(val):
        lst.append(int(input()))

    t1 = threading.Thread(target=Max,args=(lst,))
    t1.start()
    t1.join()


    t2 = threading.Thread(target = Min,args=(lst,))
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()

