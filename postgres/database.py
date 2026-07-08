import os
from contextlib import contextmanager
from sqlalchemy import create_engine, text

from dotenv import load_dotenv

load_dotenv(override=True)

# 1. Configuración de la URL de conexión
# Es buena práctica usar variables de entorno para proteger tus credenciales
DB_USER = os.getenv("DB_USER", "tu_usuario")
DB_PASS = os.getenv("DB_PASS", "tu_contraseña")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "tu_base_datos")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 2. Creación del Engine (Instancia única para toda la app)
# pool_size y max_overflow ayudan a gestionar las conexiones concurrentes en Flet
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,  # Verifica si la conexión sigue viva antes de usarla
)


# 3. Gestor de contexto para las conexiones
@contextmanager
def get_db_connection():
    """
    Proporciona una conexión limpia y asegura su cierre inmediato
    al terminar la consulta, ideal para el entorno asíncrono/concurrente de Flet.
    """
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


def test_connection():
    """
    Realiza una prueba rápida de conexión al servidor de PostgreSQL.
    Retorna True si la conexión es exitosa, False en caso contrario.
    """
    try:
        # Intentamos obtener una conexión del pool y ejecutar un SELECT básico
        with get_db_connection() as conn:
            conn.execute(text("SELECT 1"))
        print(" [OK] Conexión a PostgreSQL establecida con éxito.")
        return True
    except Exception as e:
        print(f" [ERROR] No se pudo conectar a la base de datos.")
        print(f" Detalles del error: {e}")
        return False
