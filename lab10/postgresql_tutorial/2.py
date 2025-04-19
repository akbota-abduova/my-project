import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "phonebook",
    user = "postgres",
    password = "Nn1337228"
)

cur = conn.cursor()

with open("lab10/file1.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, phone_n = line.strip().split(",")
        cur.execute("""INSERT INTO phonebook(name, phone) VALUES(%s, %s)""", (name, phone_n))

conn.commit()

cur.close()
conn.close()