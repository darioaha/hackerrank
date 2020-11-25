#https://www.hackerrank.com/challenges/matching-specific-characters
Regex_Pattern = r'^[1-3][0-2][x|s|0][0|3|A|a][x|s|u][.|,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())