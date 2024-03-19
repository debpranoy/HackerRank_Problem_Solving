n = int(input())
arr = list(map(int,input().split()))
result = 0
for num in arr:
    result = result ^ num
print(result) 
       #OR
"""
n = int(input())
arr = list(map(int,input().split()))
seen_set = set()
for num in arr:
    if num in seen_set:
        seen_set.remove(num)
    else:
        seen_set.add(num)
        
print(seen_set.pop()) """




