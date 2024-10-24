import tkinter as tk
import json
from decimal import Decimal, InvalidOperation  # Importa Decimal
from Arbol import ArbolAVL

class Actualizar:
    def __init__(self, master, inventario, panel_derecho):
        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.pack_propagate(False)
        self.frame.config(width=300, height=500)

        self.inventario = inventario
        self.panel_derecho = panel_derecho  # Referencia al panel derecho para actualizar la vista

        self.nombre_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.categoria_var = tk.StringVar()

        self.marco_formulario = tk.Frame(self.frame, bg="lightgray", padx=20, pady=20)
        self.marco_formulario.pack(padx=10, pady=10, fill="both", expand=True)

        label = tk.Label(self.marco_formulario, text="Actualizar Producto por ID", font=("Arial", 16, "bold"), bg="lightgray")
        label.pack(pady=(20, 10))

        self.create_label_entry("ID del Producto:", "id")
        
        self.btn_buscar = tk.Button(self.marco_formulario, text="Ver detalles", command=self.buscar_producto)
        self.btn_buscar.pack(pady=10)

        self.create_label_entry("Nombre:", "nombre", self.nombre_var)
        self.create_label_entry("Nueva Cantidad:", "cantidad", self.cantidad_var)
        self.create_label_entry("Nuevo Precio:", "precio", self.precio_var)
        self.create_label_entry("Categoría:", "categoria", self.categoria_var)

        self.btn_actualizar = tk.Button(self.marco_formulario, text="Actualizar Producto", command=self.actualizar_producto,
                                         bg="#4CAF50", fg="white", font=("Arial", 12), relief="raised")
        self.btn_actualizar.pack(pady=(10, 20))

        self.label_info = tk.Label(self.marco_formulario, text="", bg="lightgray", font=("Arial", 12))
        self.label_info.pack(pady=5)
            
    def buscar_producto(self):
        try:
            id_producto = int(self.entry_id.get())
        except ValueError:
            self.label_info.config(text="Por favor ingrese un número válido.")
            return

        producto = self.inventario.buscar(id_producto)

        if producto:
            cantidad = "fuera de stock" if producto['cantidad'] == 0 else str(producto['cantidad'])

            self.nombre_var.set(producto['nombre'])
            self.cantidad_var.set(cantidad)
            self.precio_var.set(str(producto['precio']))
            self.categoria_var.set(producto['categoria'])

            info = (f"ID: {id_producto}\n"
                    f"Nombre: {producto['nombre']}\n"
                    f"Cantidad: {cantidad}\n"
                    f"Precio: {producto['precio']}\n"
                    f"Categoría: {producto['categoria']}")

        else:
            self.label_info.config(text="Producto no encontrado.")
            self.clear_entries()


    def create_label_entry(self, text, entry_name, variable=None):
        label = tk.Label(self.marco_formulario, text=text, bg="lightgray", anchor="w", font=("Arial", 10))
        label.pack(fill="x", pady=(5, 0))

        if variable:
            entry = tk.Entry(self.marco_formulario, textvariable=variable, font=("Arial", 12))
        else:
            entry = tk.Entry(self.marco_formulario, font=("Arial", 12))

        entry.pack(fill="x", pady=(0, 5))
        
        setattr(self, f'entry_{entry_name}', entry)

    def actualizar_producto(self):
        try:
            id_producto = int(self.entry_id.get())
        except ValueError:
            self.label_info.config(text="Por favor ingrese un ID válido.", fg="red")
            return

        nodo = self.inventario._buscar_nodo(self.inventario.raiz, id_producto)

        if nodo:
            nuevo_nombre = self.entry_nombre.get()
            nueva_cantidad = self.entry_cantidad.get()
            nuevo_precio = self.entry_precio.get()
            nueva_categoria = self.entry_categoria.get()

            if nuevo_nombre:
                nodo.nombre = nuevo_nombre
            if nueva_cantidad:

                try:
                    nodo.cantidad = int(nueva_cantidad)
                    self.panel_derecho.dibujar_arbol()   # para actualizar la vista derecha, se cambia de color si la cantidad es cero

                except ValueError:
                    self.label_info.config(text="Por favor ingrese una cantidad válida.", fg="red")
                    return
            if nuevo_precio:
                try:
                    nodo.precio = Decimal(nuevo_precio)  # Usar Decimal para el precio
                except (ValueError, InvalidOperation):
                    self.label_info.config(text="Por favor ingrese un precio válido.", fg="red")
                    self.clear_entries()

                    return
            if nueva_categoria:
                nodo.categoria = nueva_categoria

            self.actualizar_json(id_producto, nodo)

            self.label_info.config(text="Producto actualizado correctamente.", fg="green")
            self.clear_entries()
            
        else:
            self.label_info.config(text="Producto no encontrado.", fg="red")
            self.clear_entries()

    def clear_entries(self):
        for entry_name in ["id", "nombre", "cantidad", "precio", "categoria"]:
            getattr(self, f'entry_{entry_name}').delete(0, tk.END)


    def actualizar_json(self, id_producto, nodo_actualizado):
        try:
            with open('inventario.json', 'r') as f:
                inventario = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.label_info.config(text="Error al cargar el inventario.", fg="red")
            return

        producto_actualizado = False
        for producto in inventario:
            if producto['id'] == id_producto:
                producto['nombre'] = nodo_actualizado.nombre
                producto['cantidad'] = nodo_actualizado.cantidad
                producto['precio'] = str(nodo_actualizado.precio)  # Convertir a str para JSON
                producto['categoria'] = nodo_actualizado.categoria
                producto_actualizado = True
                break

        if not producto_actualizado:
            self.label_info.config(text="Producto no encontrado en el archivo JSON.", fg="red")
            return

        with open('inventario.json', 'w') as f:
            json.dump(inventario, f, indent=4)
        self.label_info.config(text="Producto actualizado en JSON.", fg="green")

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
