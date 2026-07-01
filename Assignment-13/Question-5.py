def Grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First class"
    elif marks >=50:
        return "Second class"
    else:
        return "Fail"
def main():
    val =int(input("Enter marks :"))
    Ret = Grade(val)
    print(Ret)

if __name__ =="__main__":
    main()
