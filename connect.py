import psycopg2

def connect_to_db(host, dbname, user, password):
    """
    Establishes a connection to the PostgreSQL database server.

    Returns:
    conn: A connection object to the database, if successful.
    """
    try:
        # Устанавливаем подключение
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        print("Connection successful")
        return conn
    
    except psycopg2.OperationalError as e:
        print(f"OperationalError: {e}")
        return None

if __name__ == "__main__":
    # Определить параметры подключения
    host = "localhost"
    dbname = "finhelp"
    user = "postgres"
    password = "postgres"

    # Вызываем функцию подключения к дб
    conn = connect_to_db(host, dbname, user, password)

    if conn:
        conn.close()
