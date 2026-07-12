from multiprocessing import Pool
import os

def SumEven(no):

    sum = 0

    for i in range(2, no + 1, 2):
        sum += i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Sum of Even Numbers :", sum)
    print()

    return sum

def main():

    data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(SumEven, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()