def ChkPrime(no):
    if no == 1 or no == 0:
        return False
    for i in range(2,no):
        if no % i ==0:
            return False

    return True
