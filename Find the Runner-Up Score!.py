
n = int(input())
arr = list(map(int, input().split()))
second_max_num = max(arr)

for i in range(n):
    if second_max_num == max(arr):
        arr.remove(max(arr))
print(max(arr))

"""n = int(input())
arr = list(map(int, input().split()))
l = max(arr)
for i in range(len(arr)-1, -1, -1):
    if arr[i] < l:
        break
print(arr[i])"""



