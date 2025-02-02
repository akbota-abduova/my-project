def reverse_words():
    words = input("Введите предложение: ").split()[::-1]
    for i in range(len(words)):
        if i == len(words) - 1:
            print(words[i])  # Последнее слово без пробела
        else:
            print(words[i], end=" ")  # Остальные слова с пробелом

reverse_words()
