def miniMaxSum(arr):
    arr = list(arr)
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = map(int ,input().strip().split())

    miniMaxSum(arr)
    

"""def miniMaxSum(arr):
    l1=[]
    for i in arr:
        x=-i
        for j in arr:
            x+=j
        l1.append(x)
    print(min(l1),max(l1))    
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)"""
