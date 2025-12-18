import requests

class APIService:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        
        
    def obtener_usuarios(self):
        try:
            response = requests.get(f"{self.base_url}/users")
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return None
        
    def crear_post(self, data):
        try:
            response = requests.post(f"{self.base_url}/posts", json=data)
            return response.status_code, response.json()
        except Exception as e:
            return None, str(e)

    def actualizar_post(self, id_objeto, data):
        try:
            response = requests.put(f"{self.base_url}/posts/{id_objeto}", json=data)
            return response.status_code, response.json()
        except Exception as e:
            return None, str(e)

    def eliminar_post(self, id_objeto):
        try:
            response = requests.delete(f"{self.base_url}/posts/{id_objeto}")
            return response.status_code
        except Exception as e:
            return None
        
        
