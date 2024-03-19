def isPerfectSquare(x):
    s = int(x**0.5)
    return s*s == x

def isFibo(n):
    # Check if 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

t = int(input())
for _ in range(t):
    n = int(input())
    if isFibo(n):
        print("IsFibo")
    else:
        print("IsNotFibo")




"""
fib_list = []
    if n > 0:
        fib_list = [0]
        if n > 1:
            fib_list.append(1)
            for i in range(2, n):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list) 
"""