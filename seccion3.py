import tkinter as tk
from tkinter import font  # Para usar fuentes personalizadas
from buscarID import buscarID
from buscarPrecio import buscarPrecio
from buscarCategoria import buscarCategoria
from buscarPrecio_Categoria import buscarPrecio_Categoria
from Arbol import ArbolAVL

class Seccion3:
    def __init__(self, master, arbol):
        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.pack_propagate(False)
        self.frame.config(width=210, height=500)
        inventario = ArbolAVL()  # Inicializando el árbol AVL
        
        self.marco_formulario = tk.Frame(self.frame, bg="lightgray", padx=20, pady=20)
        self.marco_formulario.pack(padx=10, pady=10, fill="both", expand=True)
        
        label = tk.Label(self.marco_formulario, text="Consulta el inventario", font=("Arial", 16, "bold"), bg="lightgray")
        label.pack(padx=30, pady=10)


        # Crear un frame para los botones
        self.botonera = tk.Frame(self.marco_formulario, bg="#f0f0f0")  # Fondo claro
        self.botonera.pack(side="top", fill="x")  # Este frame llenará el ancho del panel

        # Establecer una fuente personalizada
        button_font = font.Font(family="Arial", size=9)
        
        # Colores para los botones
        self.default_color = "#66B2FF"  # Azul claro
        self.active_color = "#0056b3"   # Un tono más oscuro para el botón activo

        # Crear botones de navegación en horizontal
        self.btn_buscarID = tk.Button(self.botonera, text="ID", command=self.mostrar_buscarID, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_buscarID.pack(side="left", fill="x", expand=True, padx=8, pady=5)

        self.btn_buscarPrecio = tk.Button(self.botonera, text="PRECIO", command=self.mostrar_buscarPrecio, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_buscarPrecio.pack(side="left", fill="x", expand=True, padx=3, pady=5)

        self.btn_buscarCategoria = tk.Button(self.botonera, text="CATEGORIA", command=self.mostrar_buscarCategoria, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_buscarCategoria.pack(side="left", fill="x", expand=True, padx=3, pady=5)

        self.btn_buscarPrecio_Categoria = tk.Button(self.botonera, text="P & C", command=self.mostrar_buscarPrecio_Categoria, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_buscarPrecio_Categoria.pack(side="left", fill="x", expand=True, padx=3, pady=5)

        # Crear las secciones con los parámetros adecuados
        self.buscarID = buscarID(self.marco_formulario, arbol)
        self.buscarPrecio = buscarPrecio(self.marco_formulario, arbol)
        self.buscarCategoria = buscarCategoria(self.marco_formulario, arbol)
        self.buscarPrecio_Categoria = buscarPrecio_Categoria(self.marco_formulario,arbol)

        self.active_button = None
        #self.mostrar_buscarID()

    def set_active_button(self, button):
        """Establecer el botón activo y cambiar su color."""
        # Restablecer el color de todos los botones al color por defecto
        for btn in [self.btn_buscarID, self.btn_buscarPrecio, self.btn_buscarCategoria, self.btn_buscarPrecio_Categoria]:
            btn.config(bg=self.default_color)

        # Establecer el color del botón activo
        button.config(bg=self.active_color)

    def mostrar_buscarID(self):
        self.buscarID.show()
        self.buscarPrecio.hide()
        self.buscarCategoria.hide()
        self.buscarPrecio_Categoria.hide()
        self.set_active_button(self.btn_buscarID)

    def mostrar_buscarPrecio(self):
        self.buscarID.hide()
        self.buscarPrecio.show()
        self.buscarCategoria.hide()
        self.buscarPrecio_Categoria.hide()
        self.set_active_button(self.btn_buscarPrecio)

    def mostrar_buscarCategoria(self):
        self.buscarID.hide()
        self.buscarPrecio.hide()
        self.buscarCategoria.show()
        self.buscarPrecio_Categoria.hide()
        self.set_active_button(self.btn_buscarCategoria)

    def mostrar_buscarPrecio_Categoria(self):
        self.buscarID.hide()
        self.buscarPrecio.hide()
        self.buscarCategoria.hide()
        self.buscarPrecio_Categoria.show()
        self.set_active_button(self.btn_buscarPrecio_Categoria)

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
