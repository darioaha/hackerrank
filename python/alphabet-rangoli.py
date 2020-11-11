import math
def print_rangoli(size):
    alp = "abcdefghijklmnopqrstuvwxyz"
    string = alp[0:size]
    reverse = string[::-1]
    w = ((size*2)-1)+((size*2)-2)
    result = []
    for i in range(1,size+1):
        sub = reverse[:i]
        rev = sub[::-1][1:] # the first == middle char
        final = "-".join(list(sub+rev))
        final = str(final).center(w, '-')
        result.append(final)
    
    for val in result:
        print(val)
    for val in result[::-1][1:]:
        print(val)


if __name__ == '__main__':