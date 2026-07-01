def Area(radius):
    PI=3.14
    return PI * radius * radius
def main():
    val = int(input("Enter  radius :"))
    Ret = Area(val)
    print("Area of circle is :", Ret)
if __name__ =="__main__":
    main()
