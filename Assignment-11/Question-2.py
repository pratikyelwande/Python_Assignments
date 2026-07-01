def Counter(no):
    count=0
    for i in str(no):
        count += 1
    return count


def main():
    val= int(input("Enter a Number"))
    Ret = Counter(val)
    print("The Count is :", Ret)
		

if __name__ == "__main__":
	main()
