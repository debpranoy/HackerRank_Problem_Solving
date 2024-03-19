def findDigits(num):
    result = 0
    for digit in str(num):
        if digit != '0' and num % int(digit) == 0:
            result += 1
    return result

n = int(input())
for _ in range(n):
    num = int(input())
    a = findDigits(num)
    print(a)
