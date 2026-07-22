import schedule
import time
import os
import sys


def dirscanner(Dirname):

    if not os.path.exists(Dirname):
        print("Marvellous Automation Error : There is no such directory with name", Dirname)
        return

    if not os.path.isdir(Dirname):
        print("Marvellous Automation Error : It is not a directory", Dirname)
        return

    TotalFiles = 0
    SubFolders = 0

    for FolderName, SubFolder, FileName in os.walk(Dirname):
        TotalFiles += len(FileName)
        SubFolders += len(SubFolder)

    CurrentTime = time.ctime()

    print("-" * 50)
    print(f"Directory Name       : {os.path.abspath(Dirname)}")
    print(f"Total Files          : {TotalFiles}")
    print(f"Total SubDirectories : {SubFolders}")
    print(f"Scan Time            : {CurrentTime}")
    print("-" * 50)


def main():

    if len(sys.argv) != 2:

        if len(sys.argv) == 2:

            if sys.argv[1] in ("--h", "--H"):
                print("This automation script scans a directory every minute.")
                print("Use --u flag for usage.")

            elif sys.argv[1] in ("--u", "--U"):
                print("Usage :")
                print("python3 DirectoryScanner.py DirectoryName")

        else:
            print("Usage : python3 DirectoryScanner.py DirectoryName")

        return

    schedule.every(1).minutes.do(dirscanner, sys.argv[1])

    print("Directory Scanner Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
