import os
letters = [chr(i) for i in range(65, 91)]
for i in letters:
    file = open(i+'.txt', 'w')
    file.close()
    