from datos.conexion import obtener_conexion
def consultar_usuarios_respaldados():
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, username, email FROM api_users")
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res
    return []