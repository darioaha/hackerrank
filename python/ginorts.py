#https://www.hackerrank.com/challenges/ginorts/problem
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
import string

s = input()

odds = "13579"
evens = "02468"

ord1 = s.translate({ord(i): None for i in odds+evens+string.ascii_uppercase})
ord1 = ''.join(sorted(ord1))

ord2 = s.translate({ord(i): None for i in odds+evens+string.ascii_lowercase})
ord2 = ''.join(sorted(ord2))

ord3 = s.translate({ord(i): None for i in evens+string.ascii_lowercase+string.ascii_uppercase})
ord3 = ''.join(sorted(ord3))

ord4 = s.translate({ord(i): None for i in odds+string.ascii_lowercase+string.ascii_uppercase})
ord4 = ''.join(sorted(ord4))

print(ord1+ord2+ord3+ord4)