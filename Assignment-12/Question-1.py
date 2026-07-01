def vowel(x):
    char = x.lower()
    if (char == "a" or char=="i" or char=="o" or char=="u" or char=="s"):
        return True
    else:
        return False



def main():
    val = input("Enter a character:")
    ret = vowel(val)
    if (ret == True):
        print("character is vowel")
    else:
        print("Character is not vowel")


if __name__ == "__main__":
    main()
