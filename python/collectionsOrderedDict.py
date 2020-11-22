
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())

ordered_dictionary = OrderedDict()
for _ in range(n):
    items = input().rpartition(' ')
    item_name = items[0]
    net_price = int(items[2])

    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] = ordered_dictionary[item_name] + net_price
    else:
        ordered_dictionary[item_name] = net_price    
    
for key in ordered_dictionary:
    print(key,ordered_dictionary[key])