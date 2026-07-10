'''Design a Python application that creates two threads. 
Thread 1 should compute the sum of elements from a list, and Thread 2 should compute the product of elements from the same list. 
Return the results to the main thread and display them.'''

import threading
def Sum(data):
    sum=0
    for i in data:
        sum+= i
    print("Sum =" ,sum)

def Product(data):
    product=1
    for i in data:
        product *= i
    print("product =" ,product)

def main():
    data=[1,2,3,5,9,5]
    t1 = threading.Thread(target=Sum,args=(data,))
    t2 = threading.Thread(target=Product,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    main()


