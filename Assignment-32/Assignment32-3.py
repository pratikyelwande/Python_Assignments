import schedule
import time
import sys

def ReadFile(filename):
    try:
        with open(filename, "r") as fobj:

            data = fobj.read()

            if len(data) == 0:
                print("File is empty")
            else:
                print("\n----- File Contents -----")
                print(data)
                print("-------------------------")

    except FileNotFoundError:
        print("Error : File not found")

    except PermissionError:
        print("Error : Permission denied")

    except OSError:
        print("Error : Unable to open file")

    except Exception as e:
        print("Unexpected Error :", e)


def main():

    if len(sys.argv) != 2:
        print("Usage : python3 program.py <filename>")
        return

    filename = sys.argv[1]

    schedule.every(1).minutes.do(ReadFile, filename)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
