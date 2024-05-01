import psycopg2
conn = psycopg2.connect(host = "localhost", dbname = "finhelp", user = "postgres", password = "postgres", port = "5432")
cur = conn.cursor()
conn.set_session(autocommit=True)