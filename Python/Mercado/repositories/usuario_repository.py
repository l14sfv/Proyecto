class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def save(self, usuario):
        self.usuarios.append(usuario)

    def find_all(self):
        return self.usuarios

    def delete(self, nombre_usuario):
        self.usuarios = [u for u in self.usuarios if u.nombre_usuario != nombre_usuario]
        
    def find_by_nombre_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None  # Devuelve None si no se encuentra el usuario