import schedule
import time
import shutil
import os
import sys
from datetime import datetime


def backup(sourcepath, destpath):

    if not os.path.isfile(sourcepath):
        print("Source file does not exist")
        return

    if not os.path.exists(destpath):
        os.makedirs(destpath)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    filename = os.path.basename(sourcepath)
    name, extension = os.path.splitext(filename)

    backupfilename = f"{name}_{timestamp}{extension}"

    destination = os.path.join(destpath, backupfilename)

    shutil.copy2(sourcepath, destination)

    with open("backup_log.txt", "a") as fobj:
        fobj.write(
            f"Backup completed successfully at "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n"
        )

    print("Backup Created Successfully")
    print("Backup File :", destination)


def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script creates a backup of a file every hour.")
            print("Use --u flag for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage :")
            print("python3 Backup.py <SourceFile> <DestinationFolder>")

        else:
            print("Invalid Argument")

    elif len(sys.argv) == 3:

        sourcepath = sys.argv[1]
        destpath = sys.argv[2]

        schedule.every(1).minutes.do(backup, sourcepath, destpath)

        print("Backup Scheduler Started...")
        print("Press Ctrl + C to Stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")


if __name__ == "__main__":
    main()
