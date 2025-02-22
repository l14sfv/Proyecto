from entities.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioController:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def crear_usuario(self, nombres, apellidos, documento, email, telefono, nombre_usuario, contrasena):
        usuario = Usuario(nombres, apellidos, documento, email, telefono, nombre_usuario, contrasena)
        self.usuario_repository.save(usuario)

    def obtener_usuarios(self):
        return self.usuario_repository.find_all()

    def eliminar_usuario(self, nombre_usuario):
        self.usuario_repository.delete(nombre_usuario)
        