from datos.conexion import inicializar_db
import os
from negocio.gestion_usuario import registrar_nuevo_usuario, validar_login
from negocio.procesamiento import ProcesadorNegocio
import pwinput


def main():
    print("--- Iniciando Sistema API MANAGE ---")
    inicializar_db()

if __name__ == "__main__":
    main()
    


def mostrar_menu():
    print("\n--- SISTEMA API MANAGE ---")
    print("1. Registro de Usuarios ")
    print("2. Login ")
    print("3. Obtener datos de API (GET) y Respaldar ")
    print("4. Enviar datos a API (POST) ")
    print("5. Actualizar datos en API (PUT) ")
    print("6. Eliminar datos en API (DELETE) ")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    inicializar_db()
    procesador = ProcesadorNegocio()
    sesion_activa = False

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            u = input("Nuevo usuario: ")
            p = pwinput.pwinput(prompt='Ingrese su contraseña: ', mask='*')
            registrar_nuevo_usuario(u, p)

        elif opcion == "2":
            u = input("Usuario: ")
            p = pwinput.pwinput(prompt='Ingrese su contraseña: ', mask='*')
            if validar_login(u, p):
                print("¡Login exitoso! Acceso concedido.")
                sesion_activa = True
            else:
                print("Credenciales incorrectas.")

        elif opcion == "3":
            if sesion_activa:
                procesador.respaldar_datos_externos()
            else:
                print("Debe iniciar sesión primero.")
            if sesion_activa:
                procesador.respaldar_datos_externos()
            else:
                print("Error: Debe iniciar sesión (Opción 2) para realizar esta operación.")
                

        elif opcion == "4":
            if sesion_activa:
                print("\n--- Crear Nuevo Post ---")
                titulo = input("Ingrese título: ")
                cuerpo = input("Ingrese contenido: ")
                datos = {"title": titulo, "body": cuerpo, "userId": 1}
                
                status, res = procesador.servicio_api.crear_post(datos)
                if status == 201 or status == 200:
                    print(f"Éxito (Código {status}). Objeto creado: {res}")
            else:
                print("Inicie sesión primero.")

        elif opcion == "5":
            if sesion_activa:
                id_edit = input("Ingrese el ID del objeto a editar: ")
                nuevo_titulo = input("Ingrese nuevo título: ")
                datos = {"id": id_edit, "title": nuevo_titulo, "body": "Editado", "userId": 1}
                
                status, res = procesador.servicio_api.actualizar_post(id_edit, datos)
                if status == 200:
                    print(f"Éxito (Código 200). Objeto actualizado: {res}")
            else:
                print("Inicie sesión primero.")

        elif opcion == "6":
            if sesion_activa:
                id_del = input("Ingrese el ID del objeto a eliminar: ")
                status = procesador.servicio_api.eliminar_post(id_del)
                if status == 200:
                    print(f"Éxito (Código 200). El objeto {id_del} ha sido eliminado.")
            else:
                print("Inicie sesión primero.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida o aún no implementada.")

if __name__ == "__main__":
    main()