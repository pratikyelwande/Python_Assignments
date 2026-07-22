import schedule

def display():
    print("Jai Ganesh...")

def main():
    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()

if __name__ =="__main__":
    main()
