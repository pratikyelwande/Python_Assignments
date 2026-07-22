import schedule
import time
def mondaymsg():
    print("Good Morning! Start your week with enthusiasm.")
def wedmsg():
    print("Midweek check! Keep going.")
def Fridaymsg():
    print("Week completed! Have a great weekend.")

def main():
    schedule.every().monday.at("09:00").do(mondaymsg)
    schedule.every().wednesday.at("17:00").do(wedmsg)
    schedule.every().friday.at("18:00").do(Fridaymsg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
