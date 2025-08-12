import psycopg2
import sys

DB_CONFIG = {
    "dbname": "dbname",
    "user": "user",
    "password": "password",
    "host": "localhost",
    "port": "port"
}

def conectar():
   
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        sys.exit(1)
