# API_MANAGE - Evaluación Unidad 3 POO

Este proyecto es una aplicación de consola desarrollada en Python que integra conceptos de **Programación Orientada a Objetos (POO)**, gestión de bases de datos SQL y consumo de APIs externas.

## Estructura del Proyecto
[cite_start]El proyecto sigue una arquitectura modular para separar las responsabilidades[cite: 4, 6]:

* [cite_start]**auxiliares/**: Contiene constantes y validaciones del sistema[cite: 19, 48].
* [cite_start]**datos/**: Gestiona la conexión a SQLite y la persistencia de datos[cite: 20, 39].
    * [cite_start]**sql/**: Scripts DDL para la creación de tablas[cite: 50].
* [cite_start]**modelos/**: Define las clases que representan los objetos de la API[cite: 28, 63].
* [cite_start]**negocio/**: Contiene la lógica de procesamiento y encriptación de contraseñas[cite: 30, 41].
* [cite_start]**servicios/**: Encargado de las peticiones HTTP (GET, POST, PUT, DELETE) a JSONPlaceholder[cite: 34, 35].
* [cite_start]**main.py**: Punto de entrada principal con el menú interactivo[cite: 78].

## [cite_start]Funcionalidades [cite: 79]
1.  [cite_start]**Registro de Usuarios**: Almacena usuarios con contraseñas encriptadas mediante `bcrypt`[cite: 81, 82].
2.  [cite_start]**Login**: Validación de credenciales para acceder a las funciones de la API[cite: 83, 84].
3.  [cite_start]**Respaldo de API (GET)**: Obtiene datos de usuarios/tareas y los guarda en la DB local[cite: 85, 86].
4.  [cite_start]**Operaciones CRUD**: Permite crear (POST), actualizar (PUT) y eliminar (DELETE) recursos en la API externa[cite: 88, 90, 92].

## Instalación
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Ejecutar la aplicación: `python main.py`.