class Carrito:
    def __init__(self, usuario):
        self.usuario = usuario
        self.productos = []
        self.descuento = 0.0

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        total_con_descuento = total * (1 - self.descuento)
        return total_con_descuento

    def aplicar_descuento(self, descuento):
        self.descuento = descuento

    def vaciar_carrito(self):
        self.productos = []
        self.descuento = 0.0
        