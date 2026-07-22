import shutil
import os
import schedule
import time
import sys
import datetime

def Copytxtfile(source,dest):
    if not os.path.isdir(source):
        print("Source Directory does not exist")
        return
    if not os.path.isdir(dest):
        print("Destination diretory does not exist")
        return
    with open("CopyLog.txt","a") as fobj:
        fobj.write(f"\nDate :{datetime.now()}\n")
        for file in os.listdir(source):
            sourcepath = os.path.join(source,file)

            if os.path.isfile(sourcepath) and file.endwith(".txt"):
                destpath = os.path.join(dest,file)
                shutil.copy2(sourcepath,destpath)
                print(f"{file} copied successfully")
                fobj.write(f"Copied : {sourcepath} -> {destpath}\n")

            else:
                print("Unable to copy")
def main():

    if len(sys.argv) != 3:
        print("Usage : python3 program.py SourceDirectory DestinationDirectory")
        return

    source = sys.argv[1]
    destination = sys.argv[2]

    schedule.every(10).minutes.do(Copytxtfiles, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
