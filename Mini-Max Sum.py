def miniMaxSum(arr):
    arr = list(arr)
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum, max_sum)

arr = map(int, input().strip().split())
miniMaxSum(arr)
