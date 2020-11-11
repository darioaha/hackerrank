import calendar

month,day,year = map(int,input().split())

days_names = list(calendar.day_name)
n = calendar.weekday(year, month, day)
print(days_names[n].upper())
