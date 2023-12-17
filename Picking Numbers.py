def pickingNumbers(a):
    maximum = 0
    for i in a:
        x = a.count(i)
        y = a.count(i + 1)
        x = x + y
        if x > maximum:
            maximum = x
    return maximum
a = int(input())
my_list = list(map(int, input().split()))
func = pickingNumbers(my_list)
print(func)

