from multiprocessing import Pool
import os

def CountOdd(no):

    count = 0

    for i in range(1, no + 1, 2):
        count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Odd Number Count :", count)
    print()

    return count

def main():

    data = [100000, 200000, 300000, 400000]

    p = Pool()

    p.map(CountOdd, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()