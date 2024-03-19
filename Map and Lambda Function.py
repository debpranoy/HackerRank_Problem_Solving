
"""
n = int(input())
list = [0,1]
fin_list = []
for i in range(2,n):
    fibo = list[i-1] + list[i-2] 
    list.append(fibo)
for j in list:
    fin_list.append(j**3)
print(fin_list)
"""
def fibonacci(n):
    fib_list = []
    if n > 0:
        fib_list = [0]
        if n > 1:
            fib_list.append(1)
            for i in range(2, n):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

def cube(x):
    return x**3

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



    

