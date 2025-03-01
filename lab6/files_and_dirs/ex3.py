import os
t = input("Enter a path: ")
if os.access(t, os.F_OK):
    tup = os.path.split(t)
    print(f"The name of file: {tup[1]}")
    print(f"The head: {tup[0]}")
else:
    print("File does not exist") 