from functools import reduce 
from operator import mul
def mult(arr):
    n = reduce(mul, arr)
    return n
arr = list(map(int, input().split()))

print(mult(arr)) 