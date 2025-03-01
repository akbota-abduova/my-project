with open('test7.txt', 'r', encoding='utf-8') as existing, open('copied.txt', 'w', encoding='utf-8') as copied:
    copied.write(existing.read())
     