from entities.categoria import Categoria
from repositories.categoria_repository import CategoriaRepository

class CategoriaController:
    def __init__(self):
        self.categoria_repository = CategoriaRepository()

    def crear_categoria(self, nombre, descripcion):
        categoria = Categoria(nombre, descripcion)
        self.categoria_repository.save(categoria)

    def obtener_categorias(self):
        return self.categoria_repository.find_all()

    def eliminar_categoria(self, nombre):
        self.categoria_repository.delete(nombre)
        