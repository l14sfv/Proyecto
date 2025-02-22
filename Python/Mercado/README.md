# Mercado Inteligente

Este proyecto es una aplicación de gestión de un mercado inteligente, desarrollada utilizando Python y Tkinter para la interfaz gráfica de usuario (GUI). La aplicación permite gestionar usuarios, productos y categorías, así como agregar productos a un carrito de compras y calcular el total con descuentos aplicados.

## Características

- **Gestión de Usuarios**: Crear, listar y eliminar usuarios.
- **Gestión de Categorías**: Crear, listar y eliminar categorías.
- **Gestión de Productos**: Crear, listar y eliminar productos, asignándolos a categorías específicas.
- **Carrito de Compras**: Agregar productos al carrito, calcular el total y aplicar descuentos para usuarios nuevos.

## Requisitos

- Python 3.x
- Tkinter (incluido con Python)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```sh
    git clone https://github.com/l14sfv/Proyecto.git
    cd mercado-inteligente
    ```

2. (Opcional) Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate  # En Windows
    ```

3. Instala las dependencias necesarias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    python main.py
    ```

2. Interactúa con la interfaz gráfica para gestionar usuarios, categorías y productos.

## Descripción de Archivos

- **controllers/**: Contiene los controladores que manejan la lógica de negocio para usuarios, productos y categorías.
- **entities/**: Contiene las clases que representan las entidades del sistema (Usuario, Producto, Categoria).
- **repositories/**: Contiene los repositorios que manejan la persistencia de datos para usuarios, productos y categorías.
- **main.py**: Archivo principal que inicia la aplicación y define la interfaz gráfica.
- **requirements.txt**: Lista de dependencias necesarias para el proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

Para cualquier pregunta o sugerencia, por favor contacta a tu-email@example.com.