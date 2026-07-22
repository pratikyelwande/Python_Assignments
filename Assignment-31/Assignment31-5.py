import os 
import datetime
import time
import schedule
import sys

def DirCount(dirnm):
    Totalfiles=0
    for FolderName,SubFolder,FileName in os.walk(dirnm):
        Totalfiles +=len(FileName)
    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    with open("DirectoryCountLog.txt","a") as fobj:
        fobj.write(f"Directory :{os.path.abspath(dirnm)}\n")
        fobj.write(f"Total Files :{Totalfiles}\n")
        fobj.write(f"Scan Time : {CurrentTime}\n")
    print("Log Updated !")

def main():
    dirname = sys.argv[1]
    if not os.path.isdir(dirname):
        print("Invalid Directory")
        return


    schedule.every(5).minutes.do(DirCount,dirname)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()
