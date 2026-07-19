'''Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.'''
import sys

def main():
    try:
        source = sys.argv[1]
        destination = "Demo.txt"

        with open(source, "r") as fs:
            data = fs.read()

        with open(destination, "w") as fd:
            fd.write(data)

        print("Contents copied successfully.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
