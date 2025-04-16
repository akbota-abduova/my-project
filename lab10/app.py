import psycopg2

# Устанавливаем подключение к базе данных
conn = psycopg2.connect(
    dbname="phonebook", user="postgres", password="your_password", host="localhost"
)
cursor = conn.cursor()

# Создаем таблицу пользователей
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone VARCHAR(15) UNIQUE
    );
""")
conn.commit()

# Закрытие соединения
cursor.close()
conn.close()
