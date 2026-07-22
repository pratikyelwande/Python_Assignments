import os
import sys
import schedule
import time
from datetime import datetime

def DeleteEmptyFiles(directory):

    if not os.path.isdir(directory):
        print("Directory does not exist")
        return

    with open("DeletedFilesLog.txt", "a") as log:

        log.write(f"\nDate : {datetime.now()}\n")

        for FolderName, SubFolder, FileNames in os.walk(directory):

            for file in FileNames:

                filepath = os.path.join(FolderName, file)

                try:

                    if os.path.getsize(filepath) == 0:

                        os.remove(filepath)

                        print(f"Deleted : {filepath}")

                        log.write(f"Deleted : {filepath}\n")

                except Exception as e:

                    print(f"Error : {e}")

                    log.write(f"Error : {filepath} -> {e}\n")


def main():

    if len(sys.argv) != 2:
        print("Usage : python3 Assignment32-5.py DirectoryName")
        return

    directory = sys.argv[1]

    schedule.every(1).hours.do(DeleteEmptyFiles, directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
