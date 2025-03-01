import os
pat2 = input("Please enter a path: ")
def check2(pat):
    if os.access(pat, os.F_OK):  #returns true if file exists or false if it doesnt
        read = os.access(pat, os.R_OK)  #returns true if file is readable or false if its not
        write = os.access(pat, os.W_OK)  #writeability
        execute = os.access(pat, os.X_OK) 
        return [os.access(pat, os.F_OK), read, write, execute]
    
    return [False, False, False, False]

res = check2(pat2)  #[]

if res[0]:
    print(f"Existing: {res[0]}\nReadibility: {res[2]}\nWriteability: {res[2]}\nExecutability: {res[3]}")
else:
    print("File doesn't exist") 