import time

n = int(input())
t = float(input())/1000
print(f"Square root of {n} after {t*1000} milliseconds is ", end='')
def square(n, t):
    time.sleep(t)
    return n**(1/2)

print(square(n, t)) 