# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())

print(a//b)
print(a%b)
print(divmod(a,b))
