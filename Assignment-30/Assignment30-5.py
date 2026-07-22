import schedule
import datetime
import time
def display():
    fobj = open("Marvellous.txt","a")
    fobj.write("Task Executed at :"+str(datetime.datetime.now())+"\n")
    print("Current Date and Time :",datetime.datetime.now())
    fobj.close()
def main():
    schedule.every(5).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
