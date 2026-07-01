def Area(length,width):
    return length* width
def main():
    length= int(input("Enter length: "))
    width = int(input("Enter Width : "))
    Ret = Area(length,width)
    print(" Area of Rectangle is :",Ret)
if __name__ == "__main__":
    main()
