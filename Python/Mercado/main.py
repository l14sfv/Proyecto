import tkinter as tk
from tkinter import ttk, messagebox  # Importar messagebox
from controllers.usuario_controller import UsuarioController
from controllers.producto_controller import ProductoController
from controllers.categoria_controller import CategoriaController
from controllers.carrito_controller import CarritoController

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercado Inteligente")

        # Controladores
        self.usuario_controller = UsuarioController()
        self.producto_controller = ProductoController()
        self.categoria_controller = CategoriaController()
        self.carrito_controller = CarritoController()

        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Usuario
        tk.Label(self.root, text="Usuarios").grid(row=0, column=0)
        self.usuario_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, exportselection=False)  # Desactivar exportselection
        self.usuario_listbox.grid(row=1, column=0, rowspan=6)
        tk.Label(self.root, text="Nombres").grid(row=1, column=1)
        self.nombres_entry = tk.Entry(self.root)
        self.nombres_entry.grid(row=1, column=2)
        tk.Label(self.root, text="Apellidos").grid(row=2, column=1)
        self.apellidos_entry = tk.Entry(self.root)
        self.apellidos_entry.grid(row=2, column=2)
        tk.Label(self.root, text="Documento").grid(row=3, column=1)
        self.documento_entry = tk.Entry(self.root)
        self.documento_entry.grid(row=3, column=2)
        tk.Label(self.root, text="Email").grid(row=4, column=1)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=4, column=2)
        tk.Label(self.root, text="Teléfono").grid(row=5, column=1)
        self.telefono_entry = tk.Entry(self.root)
        self.telefono_entry.grid(row=5, column=2)
        tk.Label(self.root, text="Nombre de Usuario").grid(row=6, column=1)
        self.nombre_usuario_entry = tk.Entry(self.root)
        self.nombre_usuario_entry.grid(row=6, column=2)
        tk.Label(self.root, text="Contraseña").grid(row=7, column=1)
        self.contrasena_entry = tk.Entry(self.root, show="*")
        self.contrasena_entry.grid(row=7, column=2)
        tk.Button(self.root, text="Agregar Usuario", command=self.agregar_usuario).grid(row=8, column=2)

        # Categoria
        tk.Label(self.root, text="Categorias").grid(row=0, column=3)
        self.categoria_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, exportselection=False)
        self.categoria_listbox.grid(row=1, column=3, rowspan=5)
        tk.Label(self.root, text="Nombre").grid(row=1, column=4)
        self.nombre_categoria_entry = tk.Entry(self.root)
        self.nombre_categoria_entry.grid(row=1, column=5)
        tk.Label(self.root, text="Descripción").grid(row=2, column=4)
        self.descripcion_categoria_entry = tk.Entry(self.root)
        self.descripcion_categoria_entry.grid(row=2, column=5)
        tk.Button(self.root, text="Agregar Categoria", command=self.agregar_categoria).grid(row=3, column=5)

        # Producto
        tk.Label(self.root, text="Productos").grid(row=0, column=6)
        self.producto_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, exportselection=False)  # Desactivar exportselection
        self.producto_listbox.grid(row=1, column=6, rowspan=6)
        tk.Label(self.root, text="Nombre").grid(row=1, column=7)
        self.nombre_producto_entry = tk.Entry(self.root)
        self.nombre_producto_entry.grid(row=1, column=8)
        tk.Label(self.root, text="Descripción").grid(row=2, column=7)
        self.descripcion_producto_entry = tk.Entry(self.root)
        self.descripcion_producto_entry.grid(row=2, column=8)
        tk.Label(self.root, text="Precio").grid(row=3, column=7)
        self.precio_producto_entry = tk.Entry(self.root)
        self.precio_producto_entry.grid(row=3, column=8)
        tk.Label(self.root, text="Cantidad").grid(row=4, column=7)
        self.cantidad_producto_entry = tk.Entry(self.root)
        self.cantidad_producto_entry.grid(row=4, column=8)
        tk.Label(self.root, text="Categoría").grid(row=5, column=7)
        self.categoria_producto_combobox = ttk.Combobox(self.root)
        self.categoria_producto_combobox.grid(row=5, column=8)
        tk.Button(self.root, text="Agregar Producto", command=self.agregar_producto).grid(row=6, column=8)

        # Carrito
        tk.Label(self.root, text="Carrito").grid(row=9, column=0)
        self.carrito_listbox = tk.Listbox(self.root)
        self.carrito_listbox.grid(row=10, column=0, rowspan=5)
        tk.Button(self.root, text="Agregar al Carrito", command=self.agregar_al_carrito).grid(row=11, column=1)
        tk.Button(self.root, text="Calcular Total", command=self.calcular_total).grid(row=12, column=1)
        self.total_label = tk.Label(self.root, text="Total: $0.0")
        self.total_label.grid(row=13, column=1)

        # Actualizar listas al iniciar
        self.actualizar_listas()

    def agregar_usuario(self):
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        documento = self.documento_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()
        nombre_usuario = self.nombre_usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        self.usuario_controller.crear_usuario(nombres, apellidos, documento, email, telefono, nombre_usuario, contrasena)
        self.actualizar_listas()

    def agregar_categoria(self):
        nombre_categoria = self.nombre_categoria_entry.get()
        descripcion = self.descripcion_categoria_entry.get()
        self.categoria_controller.crear_categoria(nombre_categoria, descripcion)
        self.actualizar_listas()

    def agregar_producto(self):
        try:
            nombre = self.nombre_producto_entry.get()
            descripcion = self.descripcion_producto_entry.get()
            precio = float(self.precio_producto_entry.get())
            cantidad = int(self.cantidad_producto_entry.get())
            nombre_categoria = self.categoria_producto_combobox.get()
            if not nombre or not descripcion or not nombre_categoria:
                raise ValueError("Todos los campos son obligatorios.")
            self.producto_controller.crear_producto(nombre, descripcion, precio, cantidad, nombre_categoria)
            self.actualizar_listas()
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def agregar_al_carrito(self):
        selected_user_index = self.usuario_listbox.curselection()
        selected_product_index = self.producto_listbox.curselection()
        
        if not selected_user_index:
            messagebox.showwarning("Advertencia", "Seleccione un usuario.")
            return
        if not selected_product_index:
            messagebox.showwarning("Advertencia", "Seleccione un producto.")
            return
        
        usuario = self.usuario_controller.obtener_usuarios()[selected_user_index[0]]
        producto = self.producto_controller.obtener_productos()[selected_product_index[0]]
        self.carrito_controller.agregar_producto(usuario, producto, 1)
        self.actualizar_carrito(usuario)

    def calcular_total(self):
        usuario = self.usuario_controller.obtener_usuarios()[0]  # Usar el primer usuario para simplificar
        total = self.carrito_controller.calcular_total(usuario)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def actualizar_listas(self):
        # Actualizar lista de usuarios
        self.usuario_listbox.delete(0, tk.END)
        for usuario in self.usuario_controller.obtener_usuarios():
            self.usuario_listbox.insert(tk.END, usuario.nombre_usuario)

        # Actualizar lista de categorías
        self.categoria_listbox.delete(0, tk.END)
        for categoria in self.categoria_controller.obtener_categorias():
            self.categoria_listbox.insert(tk.END, categoria.nombre)

        # Actualizar lista de productos
        self.producto_listbox.delete(0, tk.END)
        for producto in self.producto_controller.obtener_productos():
            self.producto_listbox.insert(tk.END, producto.nombre)

        # Actualizar combobox de categorías
        categorias = [categoria.nombre for categoria in self.categoria_controller.obtener_categorias()]
        self.categoria_producto_combobox['values'] = categorias

    def actualizar_carrito(self, usuario):
        self.carrito_listbox.delete(0, tk.END)
        carrito = self.carrito_controller.carrito_repository.find_by_usuario(usuario)
        if carrito:
            for producto, cantidad in carrito.productos:
                self.carrito_listbox.insert(tk.END, f"{producto.nombre} x{cantidad}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()