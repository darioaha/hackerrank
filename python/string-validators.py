if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    low = False
    up = False

    for val in s:
        if (val.isalnum()):
            alnum = True
        if val.isalpha():
            alpha = True
        if val.isdigit():
            digit = True
        if val.islower():
            low = True
        if val.isupper():
            up = True

    print(alnum)
    print(alpha)
    print(digit)
    print(low)
    print(up)
    