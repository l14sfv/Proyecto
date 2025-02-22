from entities.producto import Producto
from repositories.producto_repository import ProductoRepository
from repositories.categoria_repository import CategoriaRepository

class ProductoController:
    def __init__(self):
        self.producto_repository = ProductoRepository()
        self.categoria_repository = CategoriaRepository()

    def crear_producto(self, nombre, descripcion, precio, cantidad, nombre_categoria):
        producto = Producto(nombre, descripcion, precio, cantidad, nombre_categoria)
        self.producto_repository.save(producto)

    def obtener_productos(self):
        return self.producto_repository.find_all()

    def obtener_productos_por_categoria(self, nombre_categoria):
        categoria = self.categoria_repository.find_by_nombre(nombre_categoria)
        if categoria:
            return self.producto_repository.find_by_categoria(categoria)
        return []

    def eliminar_producto(self, nombre):
        self.producto_repository.delete(nombre)

    def actualizar_producto(self, nombre, descripcion, precio, cantidad, nombre_categoria):
        categoria = self.categoria_repository.find_by_nombre(nombre_categoria)
        if categoria:
            producto = self.producto_repository.find_by_nombre(nombre)
            if producto:
                producto.descripcion = descripcion
                producto.precio = precio
                producto.cantidad = cantidad
                producto.categoria = categoria
                self.producto_repository.update(producto)

    def obtener_producto_por_nombre(self, nombre):
        return self.producto_repository.find_by_nombre(nombre)