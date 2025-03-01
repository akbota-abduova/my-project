import os
t = input("Enter the path: ")
if os.access(t, os.F_OK):
    os.remove(t)
else:
    print("The file does not exist") 