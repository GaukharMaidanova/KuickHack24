import psycopg2
import string

print("Приветствую! Я - Alapascal, твой робот-помощник по финансовой грамотности. Я помогу определить тебе твой уровень расходов и дам полезные финансовые советы. Давай же приступим!")

# данные для подключения
dbname = "finhelp"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432" 

# Подключение к базе данных
conn = psycopg2.connect(
    dbname=dbname, 
    user=user, 
    password=password, 
    host=host, 
    port=port
)

# Создание курсора
cur = conn.cursor()

# функция для логики самого фин помощника
def fin_help(mon1, mon2, filename):
    if mon1>mon2 or mon1==mon2:
        print("Вы весьма успешно формируете свой бюджет! Ваши расходы не превышают средние расходы пользователей, находящихся в вашей стране и относящихся к вашей категории пребывания в стране.")
    else:
        print("Ваши расходы превышают средние расходы пользователей, находящихся в вашей стране и относящихся к вашей категории пребывания в стране. Вот несколько советов, которые помогут вам уменьшить расходы и более грамотно управлять своими финансами:")
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for line in data:
            print(line.strip())
        

# SQL-запрос для выборки данных
your_name = str(input("Ведите, пожалуйста, ваше имя: "))
country_name = str(input("Ведите, пожалуйста, вашу страну пребывания: "))
state = str(input("Ведите, пожалуйста, характер пребывания в стране (living/tourism/business trip): "))
money = float(input("Ведите, пожалуйста, значение ваших ежемесячных трат в стране (в тг): ")) 
query = f"SELECT average_spending FROM users WHERE country = '{country_name}' AND stay_type = '{state}';"
cur.execute(query)

# Извлечение результатов запроса
results = cur.fetchall()

# Вычисление средних трат
if results:
    total_spending = sum([row[0] for row in results if row[0] is not None])
    average_spending = total_spending / len(results)
    average_spending_mean = round(average_spending, 2)
    print(f"Средние траты в стране вашего нахождения по вашей категории прибывания: {average_spending_mean}")
    print("Ваши средние траты: ", money)
    if state == "living":
        filename = "advices_citizen.txt"
        fin_help(average_spending_mean, money, filename)
    elif state == "tourism":
        filename = "advices_tourist.txt"
        fin_help(average_spending_mean, money, filename)
    elif state == "business trip":
        filename = "advices_business_trip.txt"
        fin_help(average_spending_mean, money, filename)
else:
    print("Нет данных для расчета.")

cur.close()
conn.close()

conn.close()