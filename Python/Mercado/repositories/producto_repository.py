class ProductoRepository:
    def __init__(self):
        self.productos = []

    def save(self, producto):
        self.productos.append(producto)

    def find_all(self):
        return self.productos

    def find_by_categoria(self, categoria):
        return [p for p in self.productos if p.categoria == categoria]

    def delete(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]
        
        