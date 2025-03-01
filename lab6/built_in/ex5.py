def check(tup):
    res = all(tup)
    return res

tup = (map(bool, input().split()))

print(check(tup)) 


