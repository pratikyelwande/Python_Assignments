from multiprocessing import Pool

def SumSquare(no):
    sum = 0

    for i in range(1, no + 1):
        sum += i * i

    return sum

def main():

    data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    result = p.map(SumSquare, data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()