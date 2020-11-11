def swap_case(s):
    x = lambda x: x if not x.isalpha() else (x.lower() if x.isupper() else x.upper())
    
    return ''.join(list(map(x,s)))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)