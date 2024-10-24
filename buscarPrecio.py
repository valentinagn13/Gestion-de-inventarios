import tkinter as tk
from tkinter import ttk
from Arbol import ArbolAVL

class buscarPrecio:
    def __init__(self, master, inventario):
        # Configuración del marco principal
        self.frame = tk.Frame(master)
        self.frame.pack_propagate(False)
        self.frame.config(width=400, height=500)

        self.inventario = inventario  # Referencia al árbol AVL

        # Etiqueta de título
        label = tk.Label(self.frame, text="Buscar Productos por Rango de Precio", font=("Arial", 14))
        label.pack(pady=10)

        # Campo de entrada para el precio mínimo
        self.label_precio_min = tk.Label(self.frame, text="Precio Mínimo:")
        self.label_precio_min.pack(pady=5)
        self.entry_precio_min = tk.Entry(self.frame)
        self.entry_precio_min.pack(pady=5)

        # Campo de entrada para el precio máximo
        self.label_precio_max = tk.Label(self.frame, text="Precio Máximo:")
        self.label_precio_max.pack(pady=5)
        self.entry_precio_max = tk.Entry(self.frame)
        self.entry_precio_max.pack(pady=5)

        # Botón para buscar productos
        self.btn_buscar = tk.Button(self.frame, text="Buscar Productos", command=self.buscar_productos)
        self.btn_buscar.pack(pady=10)

        # Mostrar información de la búsqueda
        self.label_info = tk.Label(self.frame, text="", font=("Arial", 10))
        self.label_info.pack(pady=5)

        # Crear Treeview para mostrar los resultados
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Cantidad", "Precio", "Categoría"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Categoría", text="Categoría")
        
        # Ajustar el ancho de las columnas
        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=100)
        self.tree.column("Cantidad", width=80)
        self.tree.column("Precio", width=80)
        self.tree.column("Categoría", width=100)

        self.tree.pack(fill="both", expand=True, pady=10)

    def buscar_productos(self):
        # Limpiar el Treeview antes de mostrar nuevos resultados
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            # Obtener y convertir los precios a float
            precio_min = float(self.entry_precio_min.get())
            precio_max = float(self.entry_precio_max.get())
            print(f"Rango de precios: {precio_min} - {precio_max}")  # Verificar rango ingresado
        except (ValueError):
            self.label_info.config(text="Por favor ingrese precios válidos.")
            return
        
        # Llamar al método de búsqueda en el árbol AVL
        resultados = self.inventario.buscar_por_rango(precio_min, precio_max)

        if resultados:
            # Insertar resultados en el Treeview
            for producto in resultados:
                # Convertir el precio a string antes de insertarlo
                self.tree.insert("", "end", values=(producto['id'], producto['nombre'], producto['cantidad'], str(producto['precio']), producto['categoria']))
            self.label_info.config(text="Productos encontrados.")
        else:
            self.label_info.config(text="No se encontraron productos en este rango.")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
