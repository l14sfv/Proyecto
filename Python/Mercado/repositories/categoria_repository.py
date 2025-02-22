class CategoriaRepository:
    def __init__(self):
        self.categorias = []

    def save(self, categoria):
        self.categorias.append(categoria)

    def find_all(self):
        return self.categorias

    def delete(self, nombre):
        self.categorias = [c for c in self.categorias if c.nombre != nombre]
        