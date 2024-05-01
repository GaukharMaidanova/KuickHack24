import psycopg2
from psycopg2 import sql
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="finhelp", 
    user="postgres", 
    password="postgres", 
    host="localhost", 
    port="5432" 
)

conn.set_client_encoding('UTF8')
# Создание курсора
cur = conn.cursor()

# Создание таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        country VARCHAR(255),
        stay_type VARCHAR(100),
        average_spending DECIMAL
    )
""")
conn.commit()

try:
    # Ввод данных пользователем
    name = input("Введите ваше имя: ")
    country = input("Введите страну нахождения: ")
    stay_type = input("Характер пребывания (жительство, туризм, командировка): ")
    average_spending = float(input("Усредненные траты за месяц (в тенге): "))

    # Вставка данных в таблицу
    cur.execute(
        sql.SQL("INSERT INTO users (name, country, stay_type, average_spending) VALUES (%s, %s, %s, %s)"),
        (name, country, stay_type, average_spending)
    )
    conn.commit()
    print("Данные успешно сохранены.")

except Exception as e:
    print(f"Произошла ошибка: {e}")
    conn.rollback()

finally:
    # Закрытие подключения
    cur.close()
    conn.close()