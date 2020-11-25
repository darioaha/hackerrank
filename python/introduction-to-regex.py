#https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

n = int(input())

for _ in range(n):
    val = input()
    print(bool(re.match(r'^(?!0)[-|+]?\d*\.?\,?\d*?$', val)))

#  TEST CASE
#       n=5
# 1.414
# +.5486468
# 0.5.0
# 1+1.0
# 0

# True
# True
# False
# False
# False
