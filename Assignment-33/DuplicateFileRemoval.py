import os
import sys
import datetime
import schedule
import hashlib
import time
import re
import smtplib
from email.message import EmailMessage
border = "-" * 50

def DirValidation(dirpath):
    if dirpath == "":
        print("Directory path is missing.")
        return False
    if not os.path.isabs(dirpath):
        print("Please provide full path.")
        return False
    if not os.path.exists(dirpath):
        print("Directory does not exists")
        return False
    if not os.path.isdir(dirpath):
        print("This is file not a directory")
        return False
    if not os.access(dirpath,os.R_OK):
        print("Permission Denied")
        return False
    return True

def MailValidation(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern,email):
        return True
    print("Invalid Email Address")
    return False

def IntervalValidation(interval):
    if not interval.isdigit():
        print("Interval Should be numeric")
        return False
    if int(interval) <= 0:
        print("Interval should be greater than zero")
        return False
    return True

def CalculateChecksum(filename):
    with open(filename,"rb") as fobj:
        hobj = hashlib.md5()
        buffer = fobj.read(1000)
        while (len(buffer)>0):
            hobj.update(buffer)
            buffer =fobj.read(1000)
        return hobj.hexdigest()

def SendMail(logfile, receiver, body):
    sender = "mail"
    password = "PASSWORD"

    msg = EmailMessage()

    msg["Subject"] = "Duplicate File Removal Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(body)

    with open(logfile, "rb") as fobj:
        filedata = fobj.read()

    msg.add_attachment(
        filedata,
        maintype="application",
        subtype="octet-stream",
        filename=os.path.basename(logfile)
    )

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
        server.quit()

        print("Mail Sent Successfully")

    except Exception as e:
        print("Unable to send mail")
        print(e)

def DuplicateFileRemoval(dirpath,reci):
    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")
    filename = os.path.join("Marvellous","DuplicateRemovalLog_"+datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+".log")

    TotalFiles=0
    TotalDuplicate=0
    TotalDuplicatesDeleted=0
    Duplicate={}
    StartTime = datetime.datetime.now()
    EndTime = datetime.datetime.now()

    with open(filename,"w") as fobj:
        fobj.write(border+"\n")
        fobj.write("Duplicate File Removal Script")
        fobj.write(border+"\n")
        for FolderName,SubFolder,FileName in os.walk(dirpath):
            for fname in FileName:
                filepath = os.path.join(FolderName, fname)
                TotalFiles += 1
                checksum = CalculateChecksum(filepath)
                if checksum in Duplicate:
                    Duplicate[checksum].append(filepath)
                else:
                    Duplicate[checksum] = [filepath] 
        for checksum in Duplicate:
            if len(Duplicate[checksum]) > 1:
                for filepath in Duplicate[checksum][1:]:
                    try:
                        os.remove(filepath)
                        TotalDuplicate += 1
                        TotalDuplicatesDeleted += 1
                        fobj.write("Deleted File : " + filepath + "\n")
                        fobj.write("Checksum     : " + checksum + "\n")
                        fobj.write(border + "\n")
                    except Exception as e:
                        fobj.write("Unable to delete : " + filepath + "\n")
                        fobj.write(str(e) + "\n")
                        fobj.write(border + "\n")

    fobj.write("Total Files Scanned : " + str(TotalFiles) + "\n")
    fobj.write("Total Duplicate Files : " + str(TotalDuplicate) + "\n")
    fobj.write("Total Deleted Files : " + str(TotalDuplicatesDeleted) + "\n")
    fobj.write("Start Time : " + str(StartTime) + "\n")
    fobj.write("Completion Time : " + str(EndTime) + "\n")

    EndTime = datetime.datetime.now()

    body = f"""
    Jay Ganesh,

    The duplicate-file removal operation has been completed successfully.

    Operation Statistics:

    Starting time of scanning : {StartTime}
    Completion time of scanning : {EndTime}
    Directory scanned : {dirpath}
    Total number of files scanned : {TotalFiles}
    Total number of duplicate files found : {TotalDuplicate}
    Total number of duplicate files deleted : {TotalDuplicatesDeleted}

    Please find the detailed log file attached to this email.

    Regards,
    Marvellous Automation System
    """

    SendMail(filename, reci, body)
def main():
    print(border)
    print("Duplicate File Removal Script")
    print(border)

    if(len(sys.argv)) == 2:
        if (sys.argv[1] == "--h" or sys.argv[1] == "--help"):
            print("This script scans a directory, identifies duplicate files using checksums,deletes duplicate files, creates a log file, and sends the log file through email.")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--usage"):
            print("Usage:python DuplicateFileRemoval.py <DirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")
        else:
            print("Invalid Options")

    elif len(sys.argv)==4:
        dirpath = sys.argv[1]
        if (DirValidation(dirpath) == False):
            return
        if not IntervalValidation(sys.argv[2]):
            return
        interval = int(sys.argv[2])
        reci = sys.argv[3]
        if MailValidation(reci) == False:
            return
        schedule.every(interval).minute.do(DuplicateFileRemoval,dirpath,reci)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ =="__main__":
    main()
