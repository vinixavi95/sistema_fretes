import psycopg2
import psycopg2.extras

PSQL = "postgresql://postgres:postgres@postgres_db:5432/fretes"

def get_connection():
    try:
        conn = psycopg2.connect(PSQL)
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
        raise e
