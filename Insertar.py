import tkinter as tk
from tkinter import font
from Arbol import ArbolAVL

class Insertar:
    def __init__(self, master, inventario, panel_derecho):
        self.frame = tk.Frame(master, bg="#f0f0f0")  # Cambia el fondo a blanco para un aspecto más limpio
        self.frame.pack_propagate(False)  # Evita que el frame cambie de tamaño automáticamente
        self.frame.config(width=300, height=500)  # Ajusta el ancho y alto según sea necesario

        self.inventario = inventario  # Referencia al árbol AVL
        self.panel_derecho = panel_derecho  # Referencia al panel derecho para actualizar la vista
        # Marco gris para los campos de entrada
        self.marco_formulario = tk.Frame(self.frame, bg="lightgray", padx=20, pady=20)
        self.marco_formulario.pack(padx=10, pady=10, fill="both", expand=True)

        # Título
        self.titulo = tk.Label(self.marco_formulario, text="Insertar un nuevo producto", font=("Kanit", 15), bg="lightgray")
        self.titulo.pack(pady=(20, 10))

        # Campos de entrada para los datos del producto
        self.create_label_entry("ID del Producto:", "id")
        self.create_label_entry("Nombre del Producto:", "nombre")
        self.create_label_entry("Cantidad Disponible:", "cantidad")
        self.create_label_entry("Precio:", "precio")
        self.create_label_entry("Categoría:", "categoria")

        # Botón para agregar el producto (dentro del marco gris)
        self.btn_agregar = tk.Button(self.marco_formulario, text="Agregar Producto", command=self.agregar_producto,
                                     bg="#4CAF50", fg="white", font=("Arial", 12), borderwidth=2, relief="groove")
        self.btn_agregar.pack(pady=(10, 10))  # Espaciado dentro del marco gris
        #self.btn_agregar.bind("<Enter>", self.on_enter)  # Efecto al pasar el mouse
        #self.btn_agregar.bind("<Leave>", self.on_leave)  # Efecto al salir el mouse

        # Mostrar un mensaje de confirmación (dentro del marco gris)
        self.label_mensaje = tk.Label(self.marco_formulario, text="", font=("Arial", 10), bg="lightgray")
        self.label_mensaje.pack(pady=5)

    def create_label_entry(self, text, entry_name):
        """Crea una etiqueta y un campo de entrada dentro del marco gris."""
        label = tk.Label(self.marco_formulario, text=text, bg="lightgray", anchor="w", font=("Arial", 10))
        label.pack(fill="x", pady=(5, 0))

        entry = tk.Entry(self.marco_formulario)
        entry.pack(fill="x", pady=(0, 5))
        
        # Almacenar la referencia del Entry en el objeto
        setattr(self, f'entry_{entry_name}', entry)

    def agregar_producto(self):
        # Obtener los datos de los campos de entrada
        try:
            id_producto = int(self.entry_id.get())
            nombre = self.entry_nombre.get()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())  # Cambiado a float para precios
            categoria = self.entry_categoria.get()

            # Verificar si el producto con el mismo ID ya existe en el árbol AVL
            if self.inventario.buscar(id_producto):
                # Si ya existe, mostrar mensaje de advertencia
                self.label_mensaje.config(text="Error: El producto con el id ya existe.", fg="red")
            else:
                # Si no existe, insertar el nuevo producto en el árbol AVL
                self.inventario.insertar(id_producto, nombre, cantidad, precio, categoria)
                self.label_mensaje.config(text="Producto agregado correctamente!", fg="green")

                # Actualizar la visualización gráfica del árbol
                self.panel_derecho.dibujar_arbol()

            # Limpiar los campos de entrada
            self.clear_entries()

        except ValueError:
            self.label_mensaje.config(text="Error: Datos inválidos. Verifique los campos.", fg="red")

    def clear_entries(self):
        """Limpia los campos de entrada."""
        for entry_name in ["id", "nombre", "cantidad", "precio", "categoria"]:
            getattr(self, f'entry_{entry_name}').delete(0, tk.END)

    # def on_enter(self, event):
    #     """Cambiar el color del botón al pasar el mouse."""
    #     event.widget['bg'] = '#0056b3'  # Un tono más oscuro

    # def on_leave(self, event):
    #     """Restaurar el color original del botón al salir el mouse."""
    #     event.widget['bg'] = '#4CAF50'  # Color original

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
