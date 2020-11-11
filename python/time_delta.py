#!/bin/python3

import math
import os
import random
import re
import sys
import calendar
from datetime import datetime, timedelta
# from pytz import timezone

def time_delta(t1, t2, monthNames):
    # Esta solucion no termina en un tiempo adecuado
    # day1, dd1, month1, year1, time1, zone1 = t1.split()
    # day2, dd2, month2, year2, time2, zone2 = t2.split()
    # hh1,mm1,ss1=map(str,time1.split(":"))
    # hh2,mm2,ss2=map(str,time2.split(":"))
    
    # M1 = int(monthNames.index(month1)) 
    # M1 = "{:02d}".format(M1)
    # M2 = int(monthNames.index(month2))
    # M2 = "{:02d}".format(M2)
    # str1 = year1+'-'+M1+'-'+dd1+' '+hh1+':'+mm1+':'+ss1+'.000'+zone1[0:3]+':'+zone1[3:5]
    # str2 = year2+'-'+M2+'-'+dd2+' '+hh2+':'+mm2+':'+ss2+'.000'+zone2[0:3]+':'+zone2[3:5]
    # dt1 = datetime.fromisoformat(str1)
    # dt2 = datetime.fromisoformat(str2)

    fmt = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1,fmt)
    dt2 = datetime.strptime(t2,fmt)

    # dt1 = dt1 + timedelta(hours=6)
    # dt2 = dt2 + timedelta(hours=11)

    # print("dt1",dt1)
    # print("dt2",dt2)
    diff = dt1 - dt2
    return str(int(abs(diff.total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    # No es necesario
    monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2, monthNames)
        fptr.write(delta + '\n')
    fptr.close()
