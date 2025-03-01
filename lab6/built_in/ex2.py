def check(s):
    upper = len(list(filter(str.isupper, s))) # filter - built-in function
    lower = len(list(filter(str.islower, s)))

    print(f"Count of upper case: {upper}")
    print(f"Count of lower case: {lower}")

s = input()

check(s) 
