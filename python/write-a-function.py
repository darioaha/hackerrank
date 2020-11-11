def is_leap(year):
    leap = False
    by4 = year % 4 == 0
    by100 = year % 100 == 0
    by400 = year % 400 == 0

    if by4 and not by100:
        return True
    elif by4 and by100 and by400:
        return True
    return False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))