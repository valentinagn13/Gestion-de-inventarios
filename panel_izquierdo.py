import tkinter as tk
from tkinter import font  # Para usar fuentes personalizadas
from Insertar import Insertar
from actualizar import Actualizar
from seccion3 import Seccion3
from seccion4 import Seccion4
from Arbol import ArbolAVL

class PanelIzquierdo:
    def __init__(self, master, arbol, panel_derecho):
        self.master = master
        
        # PANEL DE CONTENIDO COLOR lightblue
        self.panel = tk.Frame(master)
        self.panel.pack(fill="both", expand=True)
        inventario = ArbolAVL()  # Inicializando el árbol AVL
        # Título
        self.img_insertar5 = tk.PhotoImage(file="la-gestion-del-inventario (1).png") 

        self.titulo = tk.Label(self.panel, image=self.img_insertar5, compound="right", text="SISTEMA DE GESTIÓN DE INVENTARIO  ", font=("Arial", 13, "bold"), bg="#f0f0f0")
        self.titulo.pack(pady=(20, 10))

        # Crear un frame para los botones
        self.botonera = tk.Frame(self.panel)
        self.botonera.pack(side="top", fill="x")  # Este frame llenará el ancho del panel

        # Establecer una fuente personalizada
        button_font = font.Font(family="Arial", size=12, weight="bold")

        # Crear un color para los botones
        self.default_color = "#007BFF"  # Color azul
        self.active_color = "#0056b3"  # Un tono más oscuro para el botón activo
        self.img_insertar1 = tk.PhotoImage(file="insertar.png") 
        self.img_insertar2 = tk.PhotoImage(file="actualizar-base-de-datos.png") 
        self.img_insertar3 = tk.PhotoImage(file="lupa (1).png") 
        self.img_insertar4 = tk.PhotoImage(file="eliminar.png") 


        # Crear el botón Insertar con imagen y texto
        self.btn_insertar = tk.Button(self.botonera, text="Insertar", image=self.img_insertar1, compound="left",command=self.mostrar_insertar, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_insertar.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.btn_actualizar = tk.Button(self.botonera, text="Actualizar",image=self.img_insertar2, compound="left", command=self.mostrar_actualizar, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_actualizar.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.btn_seccion3 = tk.Button(self.botonera, text="Buscar", image=self.img_insertar3, compound="left", command=self.mostrar_seccion3, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_seccion3.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.btn_seccion4 = tk.Button(self.botonera, text="Eliminar",image=self.img_insertar4, compound="left", command=self.mostrar_seccion4, font=button_font, bg=self.default_color, fg="white", borderwidth=2, relief="groove")
        self.btn_seccion4.pack(side="left", fill="x", expand=True, padx=5, pady=5)


        # Crear las secciones con los parámetros adecuados
        self.insertar = Insertar(self.panel, arbol, panel_derecho)
        self.actualizar = Actualizar(self.panel, arbol, panel_derecho)
        self.seccion3 = Seccion3(self.panel, arbol)
        self.seccion4 = Seccion4(self.panel, arbol, panel_derecho)

        # Inicializar el botón activo
        self.active_button = None

        # Mostrar la primera sección por defecto
        self.mostrar_insertar()

    def set_active_button(self, button):
        """Establecer el botón activo y cambiar su color."""
        # Restablecer el color de todos los botones
        for btn in [self.btn_insertar, self.btn_actualizar, self.btn_seccion3, self.btn_seccion4]:
            btn.config(bg=self.default_color)

        # Establecer el color del botón activo
        button.config(bg=self.active_color)

    def mostrar_insertar(self):
        self.insertar.show()
        self.actualizar.hide()
        self.seccion3.hide()
        self.seccion4.hide()
        self.set_active_button(self.btn_insertar)  # Resaltar el botón activo

    def mostrar_actualizar(self):
        self.insertar.hide()
        self.actualizar.show()
        self.seccion3.hide()
        self.seccion4.hide()
        self.set_active_button(self.btn_actualizar)  # Resaltar el botón activo

    def mostrar_seccion3(self):
        self.insertar.hide()
        self.actualizar.hide()
        self.seccion3.show()
        self.seccion4.hide()
        self.set_active_button(self.btn_seccion3)  # Resaltar el botón activo

    def mostrar_seccion4(self):
        self.insertar.hide()
        self.actualizar.hide()
        self.seccion3.hide()
        self.seccion4.show()
        self.set_active_button(self.btn_seccion4)  # Resaltar el botón activo
