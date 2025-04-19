import csv
import psycopg2

def upload_csv_to_db(csv_file):
    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
        dbname="phonebook", user="postgres", password="your_password", host="localhost"
    )
    cursor = conn.cursor()

    # Открываем CSV файл и считываем данные
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропускаем строку с заголовками

        # Вставляем данные из CSV в таблицу
        for row in csv_reader:
            cursor.execute("INSERT INTO users (first_name, last_name, phone) VALUES (%s, %s, %s)", row)

    # Подтверждаем изменения и закрываем соединение
    conn.commit()
    cursor.close()
    conn.close()

# Укажите путь к вашему CSV файлу
upload_csv_to_db('phonebook.csv')
