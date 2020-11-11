def count_substring(string, sub_string):
    # testString1.find('l',4,9)    
    count = 0
    init = 0
    while True:
        idx = string.find(sub_string,init)
        if (idx != -1):
            count +=1
        else:
            break
        init = idx + 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)