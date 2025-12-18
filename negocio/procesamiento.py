from servicios.api_service import APIService
from datos.insertar_datos import guardar_usuarios_api
from datos.obtener_datos import consultar_usuarios_respaldados

class ProcesadorNegocio:
    def __init__(self):
        self.servicio_api = APIService()

    def respaldar_datos_externos(self):
        """Esta es la función que busca main.py"""
        print("Obteniendo datos de la API externa...")
        usuarios_json = self.servicio_api.obtener_usuarios()
        
        if usuarios_json:
            guardar_usuarios_api(usuarios_json)
            
            print("\n--- DATOS RESPALDADOS EN MySQL ---")
            datos_locales = consultar_usuarios_respaldados()
            for u in datos_locales:
                print(f"ID: {u[0]} | Nombre: {u[1]} | Email: {u[3]}")
        else:
            print("No se pudieron obtener datos de la API.")