import csv

# Данные для записи в CSV
data = [
    ["first_name", "last_name", "phone"],
    ["John", "Doe", "1234567890"],
    ["Jane", "Smith", "0987654321"],
    ["Alice", "Johnson", "5551234567"]
]

# Открываем файл для записи (если файл не существует, он будет создан)
with open("phonebook.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Записываем данные в файл
    writer.writerows(data)
