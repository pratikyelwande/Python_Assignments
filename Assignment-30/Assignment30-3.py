import schedule

def display():
    print("Coding Karr..")

def main():
    schedule.every(30).minute.do(display)

    while True:
        schedule.run_pending()

if __name__ =="__main__":
    main()
