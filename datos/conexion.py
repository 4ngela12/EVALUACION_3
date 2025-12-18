import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'API_MANAGE'
        }
        conn = mysql.connector.connect(**config)
        return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def inicializar_db():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sistema_usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario VARCHAR(100) UNIQUE NOT NULL,
                    password_hash BLOB NOT NULL
                )
            ''')
            conexion.commit()
            print("Base de datos inicializada correctamente.")
        except Error as e:
            print(f"Error al inicializar tablas: {e}")
        finally:
            cursor.close()
            conexion.close()