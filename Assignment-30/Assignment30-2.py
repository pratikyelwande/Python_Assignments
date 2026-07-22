import schedule
import datetime

def display():
    print("Current Date and Time :",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(display)

    while True:
        schedule.run_pending()

if __name__ =="__main__":
    main()
