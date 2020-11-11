def print_formatted(number):
    w = len(bin(number)[2:])
    for val in range(1,number+1):
        dec = str(val).rjust(w, ' ')
        octal = str(oct(val)[2:]).rjust(w, ' ')
        hexa = str(hex(val)[2:]).upper().rjust(w, ' ')
        bina = str(bin(val)[2:]).rjust(w, ' ')
        
        print(dec,octal,hexa,bina)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)