def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]  # Убираем i-й символ
        permute(new_s, answer + s[i])  # Рекурсивный вызов с добавлением символа

user_input = input("Введите строку: ")
permute(user_input)
 