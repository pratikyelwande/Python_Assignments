def main():
    try:
        filename = input("Enter File Name : ")
        word = input("Enter Word : ")

        with open(filename, "r") as fobj:
            data = fobj.read()

        words = data.split()

        count = 0

        for w in words:
            if w == word:
                count += 1

        print("Frequency of", word, "is:", count)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
