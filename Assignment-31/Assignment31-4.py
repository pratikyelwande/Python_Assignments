import schedule
import datetime
import time
def work():
    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    name = f"MarvellousLog_{timestamp}.txt"
    with open(name,"w") as fobj:
        fobj.write(f"Creation Time :{datetime.datetime.now()}")
    
    print("Log file created successfully.")
def main():

    schedule.every(10).minutes.do(work)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ =="__main__":
    main()
