class CarritoRepository:
    def __init__(self):
        self.carritos = []

    def save(self, carrito):
        self.carritos.append(carrito)

    def find_by_usuario(self, usuario):
        for carrito in self.carritos:
            if carrito.usuario == usuario:
                return carrito
        return None

    def delete(self, carrito):
        self.carritos.remove(carrito)

    def update(self, carrito):
        for i, c in enumerate(self.carritos):
            if c.id == carrito.id:
                self.carritos[i] = carrito
                break
            