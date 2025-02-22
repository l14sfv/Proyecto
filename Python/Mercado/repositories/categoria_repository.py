class CategoriaRepository:
    def __init__(self):
        self.categorias = []

    def save(self, categoria):
        self.categorias.append(categoria)

    def find_all(self):
        return self.categorias

    def find_by_nombre(self, nombre):
        for categoria in self.categorias:
            if categoria.nombre == nombre:
                return categoria
        return None

    def delete(self, nombre):
        self.categorias = [c for c in self.categorias if c.nombre != nombre]
        
        