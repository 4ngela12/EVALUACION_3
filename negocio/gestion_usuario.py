from datos.conexion import obtener_conexion
from negocio.encriptacion import Encriptador

def registrar_nuevo_usuario(username, password):
    encriptador = Encriptador()
    pw_hash = encriptador.encriptar_password(password)
    
    conn = obtener_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO sistema_usuarios (usuario, password_hash) VALUES (%s, %s)"
            cursor.execute(sql, (username, pw_hash))
            conn.commit()
            print("Usuario registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar: {e}")
        finally:
            cursor.close()
            conn.close()

def validar_login(username, password_plana):
    conn = obtener_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT password_hash FROM sistema_usuarios WHERE usuario = %s"
            cursor.execute(sql, (username,))
            resultado = cursor.fetchone()
            if resultado:
                return Encriptador.verificar_password(password_plana, resultado[0])
        finally:
            cursor.close()
            conn.close()
    return False