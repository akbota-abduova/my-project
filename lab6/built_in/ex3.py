def ispalindrom(s):
    t = reversed(s) 
    k = ""
    i = iter(t)
    for j in i:
        k+=j
    
    if k==s: return True 
    return False
s = input()

if ispalindrom(s): print("Yes, it is a palindrome")
else: print("No, it is not a palindrome")