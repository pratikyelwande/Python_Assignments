#Design a Python application that creates two threads named EvenFactor and OddFactor.
#Both threads should accept one integer number as a parameter.
#The EvenFactor thread should:
#Identify all even factors of the given number.
#Calculate and display the sum of even factors.
#The OddFactor thread should:Identify all odd factors of the given number.
#Calculate and display the sum of odd factors.After both threads complete execution, the main thread should display the message:


import threading

def EvenFactor(no):
    sum=0
    for i in range(2,no+1,2):
        if no % i ==0:
            print(i)
            sum += i
            print("Even Sum is : ",sum)
        

def OddFactor(no):
    sum=0
    for i in range(1,no+1,2):
        if no % i == 0:
            print(i)
            sum += i
            print("Odd sum is : ",sum)

def main():
    t1 = threading.Thread(target = EvenFactor, args=(11000,))
    t2 = threading.Thread(target= OddFactor, args =(1200,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    main()

