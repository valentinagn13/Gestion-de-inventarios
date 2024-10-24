import tkinter as tk
from tkinter import ttk
from Arbol import ArbolAVL

class buscarCategoria:
    def __init__(self, master, inventario):
        # Configuración del marco principal
        self.frame = tk.Frame(master)
        self.frame.pack_propagate(False)
        self.frame.config(width=400, height=500)

        self.inventario = inventario  # Referencia al árbol AVL

        # Etiqueta de título
        label = tk.Label(self.frame, text="Buscar Productos por Categoría", font=("Arial", 14))
        label.pack(pady=10)

        # Campo de entrada para la categoría
        self.label_categoria = tk.Label(self.frame, text="Categoría:")
        self.label_categoria.pack(pady=5)
        self.entry_categoria = tk.Entry(self.frame)
        self.entry_categoria.pack(pady=5)

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

        # Obtener la categoría ingresada
        categoria = self.entry_categoria.get().strip()
        
        if not categoria:
            self.label_info.config(text="Por favor ingrese una categoría válida.")
            return
        
        # Llamar al método de búsqueda en el árbol AVL
        resultados = self.inventario.buscar_por_categoria(categoria)

        if resultados:
            # Insertar resultados en el Treeview
            for producto in resultados:
                self.tree.insert("", "end", values=(producto['id'], producto['nombre'], producto['cantidad'], producto['precio'], producto['categoria']))
            self.label_info.config(text="Productos encontrados.")
        else:
            self.label_info.config(text="No se encontraron productos en esta categoría.")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
