'''Design a Python application that creates three threads named Small, Capital, and Digits.
All threads should accept a string as input.
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters.
The Digits thread should count and display the number of numeric digits.
Each thread must also display:
Thread ID
Thread Name'''


import threading

def checklower(no):
    thread= threading.current_thread()
    print(f"Thread ID is {thread.ident}")
    print(f"Thread Name is {thread.name}")
    count=0
    for i in no:
        if i.islower():
            count += 1
    print("LowerCase Characters :",count)
             
def checkupper(no):
    thread= threading.current_thread()
    print(f"Thread ID is {thread.ident}")
    print(f"Thread Name is {thread.name}")
    count=0
    for i in no:
        if i.isupper():
            count +=1
    print("Uppercase characters : ",count)

def checkdigit(no):
    thread= threading.current_thread()
    print(f"Thread ID is {thread.ident}")
    print(f"Thread Name is {thread.name}")
    count =0
    for i in no:
        if i.isdigit():
            count += 1
    print("Digits : ",count)


def main():
    thread= threading.current_thread()
    print(f"Thread ID is {thread.ident}")
    print(f"Thread Name is {thread.name}")
    
    val = input("Enter String : ")

    small = threading.Thread(target = checklower, args=(val,),name="small")
    capital = threading.Thread(target= checkupper, args =(val,),name="capital")
    digit = threading.Thread(target = checkdigit, args=(val,),name="digit")

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

if __name__ == "__main__":
    main()

