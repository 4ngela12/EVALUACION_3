class UsuarioAPI:
    def __init__(self, id, name, username, email):
        self.id = id
        self.nombre = name
        self.usuario_nick = username
        self.email = email

class Tarea:
    def __init__(self, id, userId, title, completed):
        self.id = id
        self.id_usuario = userId
        self.titulo = title
        self.completada = completed

class Usuario:
    def __init__(self, username, password_encriptada):
        self.username = username
        self.password = password_encriptada