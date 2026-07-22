import schedule
import datetime
import time

def Create():
    filename = f"File_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.txt"  
    fobj = open(filename,"w")
    fobj.write(filename)
    fobj.close()

def main():
    schedule.every(1).minutes.do(Create)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
