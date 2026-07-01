def reverse(no):
    for i in range(no,0,-1):
        print(i, end=" ")

def main():
    val = int(input("Enter a number : "))
    reverse(val)

if __name__ == "__main__":
    main()

