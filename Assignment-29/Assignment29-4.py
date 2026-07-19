

import sys

def main():
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        with open(file1, "r") as f1:
            data1 = f1.read()

        with open(file2, "r") as f2:
            data2 = f2.read()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
