from datos.conexion import obtener_conexion

def guardar_usuarios_api(lista_usuarios):
    conn = obtener_conexion()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT IGNORE INTO api_users (id, name, username, email) VALUES (%s, %s, %s, %s)"
            
            for u in lista_usuarios:
                valores = (u['id'], u['name'], u['username'], u['email'])
                cursor.execute(sql, valores)
            
            conn.commit()
            print(f"Éxito: {len(lista_usuarios)} usuarios procesados.")
        finally:
            cursor.close()
            conn.close()