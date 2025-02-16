from datetime import datetime

date1_str = input("first date (YYYY-MM-DD HH:MM:SS): ") #2025-02-16 14:30:45
date2_str = input("second date (YYYY-MM-DD HH:MM:SS): ")

# Преобразование строк в объекты datetime
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Вычисляем разницу
difference = abs((date1 - date2).total_seconds())

print("difference in seconds:", difference)


