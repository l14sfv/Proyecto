from entities.carrito import Carrito
from repositories.carrito_repository import CarritoRepository
from repositories.usuario_repository import UsuarioRepository

class CarritoController:
    def __init__(self):
        self.carrito_repository = CarritoRepository()
        self.usuario_repository = UsuarioRepository()

    def crear_carrito(self, usuario):
        carrito = Carrito(usuario)
        if self.usuario_repository.find_by_nombre_usuario(usuario.nombre_usuario) is None:
            carrito.aplicar_descuento(0.10)  # Descuento del 10% para usuarios nuevos
        self.carrito_repository.save(carrito)
        return carrito

    def agregar_producto(self, usuario, producto, cantidad):
        carrito = self.carrito_repository.find_by_usuario(usuario)
        if carrito is None:
            carrito = self.crear_carrito(usuario)
        carrito.agregar_producto(producto, cantidad)
        return carrito

    def calcular_total(self, usuario):
        carrito = self.carrito_repository.find_by_usuario(usuario)
        if carrito:
            return carrito.calcular_total()
        return 0.0
    