from collections import Counter

k=input()

count_items = Counter(input().split())

for key,count in count_items.items():
    if count==1:
        print(key)