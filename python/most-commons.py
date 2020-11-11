#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    arrCount = Counter(sorted(s))
    for val in arrCount.most_common(3):
        print(val[0],val[1])
