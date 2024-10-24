import tkinter as tk
from tkinter import ttk
from Arbol import ArbolAVL

class buscarID:
    def __init__(self, master, inventario):
        # Configuración del marco principal
        self.frame = tk.Frame(master)
        self.frame.pack_propagate(False)
        self.frame.config(width=400, height=500)

        self.inventario = inventario  # Referencia al árbol AVL

        # Etiqueta de título
        label = tk.Label(self.frame, text="Buscar un producto", font=("Arial", 14))
        label.pack(pady=10)

        # Campo de entrada para el ID del producto
        self.label_id = tk.Label(self.frame, text="ID del Producto:")
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(self.frame)
        self.entry_id.pack(pady=5)

        # Botón para buscar el producto
        self.btn_buscar = tk.Button(self.frame, text="Buscar Producto", command=self.buscar_producto)
        self.btn_buscar.pack(pady=10)

        # Mostrar información del producto
        self.label_info = tk.Label(self.frame, text="", font=("Arial", 10))
        self.label_info.pack(pady=5)

        # Crear Treeview para mostrar los resultados
        self.tree = ttk.Treeview(self.frame, columns=("Nombre", "Cantidad", "Precio", "Categoría"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Categoría", text="Categoría")
        
        # Ajustar el ancho de las columnas
        self.tree.column("Nombre", width=100)
        self.tree.column("Cantidad", width=80)
        self.tree.column("Precio", width=80)
        self.tree.column("Categoría", width=100)

        self.tree.pack(fill="both", expand=True, pady=10)

    def buscar_producto(self):
        # Limpiar el Treeview antes de mostrar nuevos resultados
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            # Obtener el ID del campo de entrada y convertir a entero
            id_producto = int(self.entry_id.get())
            print(f"ID a buscar desde la entrada: {id_producto}")  # Verificar ID ingresado
        except ValueError:
            self.label_info.config(text="Por favor ingrese un número válido.")
            return
        
        # Llamar al método de búsqueda en el árbol AVL
        resultado = self.inventario.buscar(id_producto)
        if resultado:
            # Insertar resultados en el Treeview
            self.tree.insert("", "end", values=(resultado['nombre'], resultado['cantidad'], resultado['precio'], resultado['categoria']))
            self.label_info.config(text="Producto encontrado.")
        else:
            self.label_info.config(text="Producto no encontrado.")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
