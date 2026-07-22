import schedule
import datetime
import time
import os
import sys

def MonitorSize(filename):

    if os.path.exists(filename):

        path = os.path.abspath(filename)
        size = os.path.getsize(filename)
        CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        with open("FileSizeLog.txt", "a") as fobj:
            fobj.write(f"File Path : {path}\n")
            fobj.write(f"File Size : {size} Bytes\n")
            fobj.write(f"Date Time : {CurrentTime}\n")
            fobj.write("-" * 40 + "\n")

        print("Log Updated Successfully")

    else:
        print("File does not exist")

def main():

    if len(sys.argv) != 2:
        print("Usage : python3 program.py <filename>")
        return

    schedule.every(30).seconds.do(MonitorSize, sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
