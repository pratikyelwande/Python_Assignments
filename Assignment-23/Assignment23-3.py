from multiprocessing import Pool
import os

def CountEven(no):

    count = 0

    for i in range(2, no + 1, 2):
        count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Even Number Count :", count)
    print()

    return count

def main():

    data = [100000, 200000, 300000, 400000]

    p = Pool()

    p.map(CountEven, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()