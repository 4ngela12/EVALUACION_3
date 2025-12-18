import bcrypt

class Encriptador:
    @staticmethod
    def encriptar_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    @staticmethod
    def verificar_password(password_plana, password_encriptada):
        return bcrypt.checkpw(password_plana.encode('utf-8'), password_encriptada)