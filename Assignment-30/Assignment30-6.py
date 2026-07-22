import schedule
import datetime
import time
def lunch():
    print("Lunch Time!")
def wrap():
    print("Wrap up Work!")
def main():
    schedule.every().day.at.("1.00")do(lunch)
    schedule.every().day.at.("6.00").do(wrap)


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
