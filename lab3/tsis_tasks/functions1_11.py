def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]  

word = input("Введите слово или фразу: ")
print("Палиндром" if is_palindrome(word) else "Не палиндром")
