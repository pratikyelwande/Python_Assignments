import schedule
import time
def DisplayMessage(msg):
    print(msg)    

def main():
    msg= input("Enter message :")
    interval=int(input("enter interval in seconds :"))
    if interval >0:
        schedule.every(interval).seconds.do(DisplayMessage,msg)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Interval is Zero")
    
if __name__=="__main__":
    main()
