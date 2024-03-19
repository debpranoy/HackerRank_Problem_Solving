import math
def Sherlock_and_Squares(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(Sherlock_and_Squares(a, b))

           #OR
"""import math

def Sherlock_and_Squares(a, b):
    count = 0
    for i in range(a, b+1):
        sqrt_i = int(math.sqrt(i))
        if sqrt_i**2 == i:
            count += 1
    return count

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = Sherlock_and_Squares(a, b)
    print(result)"""
                    #OR
"""import math
                                    
def Sherlock_and_Squares(a, b):
    # Find the square root of the smallest integer greater than or equal to 'a'
    start = math.ceil(math.sqrt(a))
    
    # Find the square root of the largest integer less than or equal to 'b'
    end = math.floor(math.sqrt(b))

    # Count the square integers in the range [a, b]
    count = max(0, end - start + 1)

    return count

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    a, b = map(int, input("Enter the range [A B] for test case: ").split())
    result = Sherlock_and_Squares(a, b)
    print("Count of square integers:", result)"""

                         #or
"""import math

def count_square_integers(a, b):
    count = 0
    for i in range(int(math.sqrt(a)), int(math.sqrt(b)) + 1):
        square = i**2
        if a <= square <= b:
            count += 1
    return count

# Input the number of test cases
t = int(input())

for _ in range(t):
    # Input the range [A, B] for each test case
    a, b = map(int, input().split())
    
    # Calculate and print the count of square integers in the given range
    result = count_square_integers(a, b)
    print(result)"""


