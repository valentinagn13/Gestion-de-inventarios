import tkinter as tk
from tkinter import font
from Arbol import ArbolAVL
from guardarInventario import eliminar_de_json
class Seccion4:
    def __init__(self, master, inventario, panel_derecho):
        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.pack_propagate(False)
        self.frame.config(width=300, height=400)
        
        self.inventario = inventario
        self.panel_derecho = panel_derecho
        
        self.marco_formulario = tk.Frame(self.frame, bg="lightgray", padx=20, pady=20)
        self.marco_formulario.pack(padx=10, pady=10, fill="both", expand=True)

        label = tk.Label(self.marco_formulario, text="Eliminar un Producto", font=("Arial", 16, "bold"), bg="lightgray")
        label.pack(pady=(20, 10))

        self.create_label_entry("ID del Producto:", "id")

        self.btn_eliminar = tk.Button(self.marco_formulario, text="Eliminar Producto", command=self.eliminar_producto,
                                      bg="#4CAF50", fg="white", font=("Arial", 12), relief="raised")
        self.btn_eliminar.pack(pady=(10, 20))

        self.label_info = tk.Label(self.marco_formulario, text="", bg="lightgray", font=("Arial", 12))
        self.label_info.pack(pady=5)

    def actualizar_id_producto(self, id_producto):
        """Actualizar el campo de entrada con el ID del producto a eliminar."""
        self.entry_id.delete(0, tk.END)  # Limpiar el campo de entrada
        self.entry_id.insert(0, str(id_producto))  # Insertar el ID del nodo

    def create_label_entry(self, text, entry_name):
        label = tk.Label(self.marco_formulario, text=text, bg="lightgray", anchor="w", font=("Arial", 10))
        label.pack(fill="x", pady=(5, 0))

        entry = tk.Entry(self.marco_formulario, font=("Arial", 12))
        entry.pack(fill="x", pady=(0, 5))
        
        # Almacenar la referencia del Entry en el objeto
        setattr(self, f'entry_{entry_name}', entry)

    def eliminar_producto(self):
        try:
            id_producto = int(self.entry_id.get())
        except ValueError:
            self.label_info.config(text="⚠️ Por favor ingrese un número válido.", fg="#E74C3C")
            return

        eliminado = self.inventario.eliminar(id_producto)

        if eliminado:
            eliminar_de_json(id_producto)
            self.label_info.config(text=f"✅ Producto con ID {id_producto} eliminado.", fg="#28A745")
            self.panel_derecho.dibujar_arbol()
            self.clear_entries()
        else:
            self.label_info.config(text="⚠️ Producto no encontrado.", fg="#E74C3C")
            
    def clear_entries(self):
        for entry_name in ["id"]:
            getattr(self, f'entry_{entry_name}').delete(0, tk.END)


    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()


