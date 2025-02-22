from entities.producto import Producto
from repositories.producto_repository import ProductoRepository

class ProductoController:
    def __init__(self):
        self.producto_repository = ProductoRepository()

    def crear_producto(self, nombre, descripcion, precio, cantidad):
        producto = Producto(nombre, descripcion, precio, cantidad)
        self.producto_repository.save(producto)

    def obtener_productos(self):
        return self.producto_repository.find_all()

    def eliminar_producto(self, nombre):
        self.producto_repository.delete(nombre)
        