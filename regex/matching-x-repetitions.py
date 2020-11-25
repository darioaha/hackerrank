# https://www.hackerrank.com/challenges/matching-x-repetitions/problem
Regex_Pattern = r'^[a-zA-Z|2|4|6|8|0]{40}[1|3|5|7|9|\s]{5}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())