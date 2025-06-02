# database.py
import os
from psycopg2 import pool
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do pool de conexões
connection_pool = pool.SimpleConnectionPool(
    1,  # Mínimo de conexões
    10, # Máximo de conexões
    database=os.getenv('DB_NAME', 'estacionamento_db'),
    user=os.getenv('DB_USER', 'postgres'),
    password=os.getenv('DB_PASSWORD', 'pl4c4S!'),
    host=os.getenv('DB_HOST', 'localhost'),
    port=os.getenv('DB_PORT', '5432')
)

def get_connection():
    """Obtém uma conexão do pool"""
    return connection_pool.getconn()

def release_connection(conn):
    """Libera uma conexão de volta para o pool"""
    connection_pool.putconn(conn)

def init_db():
    """Inicializa o banco de dados criando a tabela se não existir"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS placas_placadetectada (
                    id SERIAL PRIMARY KEY,
                    placa VARCHAR(8) NOT NULL,
                    data_hora TIMESTAMP NOT NULL,
                    status VARCHAR(10) NOT NULL CHECK (status IN ('entrada', 'saida'))
                )
            """)
        conn.commit()
    finally:
        release_connection(conn)