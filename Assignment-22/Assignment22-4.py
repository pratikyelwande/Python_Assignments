from multiprocessing import Pool
import time

def SumPower(no):

    sum = 0

    for i in range(1, no + 1):
        sum += i ** 5

    return sum

def main():

    data = [1000000, 2000000, 3000000, 4000000]

    start = time.time()

    p = Pool()

    result = p.map(SumPower, data)

    p.close()
    p.join()

    end = time.time()

    print(result)
    print("Execution Time :", end - start, "seconds")

if __name__ == "__main__":
    main()