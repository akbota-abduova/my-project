import psycopg2

def insert_user():
    # Подключаемся к базе данных
    conn = psycopg2.connect(
        dbname="phonebook", user="postgres", password="your_password", host="localhost"
    )
    cursor = conn.cursor()

    # Запрашиваем имя и номер телефона
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")

    # Вставляем данные в таблицу
    cursor.execute("INSERT INTO users (first_name, last_name, phone) VALUES (%s, %s, %s)", 
                   (first_name, last_name, phone))

    # Подтверждаем изменения и закрываем соединение
    conn.commit()
    cursor.close()
    conn.close()

insert_user()
